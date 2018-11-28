using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
// for Thread.Sleep
using System.Threading;

// Reference the API
using ThingMagic;

namespace ReadAsyncTrack
{
    /// <summary>
    /// Sample program that reads tags in the background and track tags
    /// that have been seen; only print the tags that have not been seen
    /// before.
    /// </summary>
    class Program
    {
        static void Usage()
        {
            Console.WriteLine(String.Join("\r\n", new string[] {
                    "Usage: "+"Please provide valid arguments, such as:",
                    "tmr:///com4 or tmr:///com4 --ant 1,2",
                    "tmr://my-reader.example.com or tmr://my-reader.example.com --ant 1,2"
            }));
            Environment.Exit(1);
        }
        static void Main(string[] args)
        {
            // Program setup
            if (1 > args.Length)
            {
                Usage();
            }
            int[] antennaList = null;
            for (int nextarg = 1; nextarg < args.Length; nextarg++)
            {
                string arg = args[nextarg];
                if (arg.Equals("--ant"))
                {
                    if (null != antennaList)
                    {
                        Console.WriteLine("Duplicate argument: --ant specified more than once");
                        Usage();
                    }
                    antennaList = ParseAntennaList(args, nextarg);
                    nextarg++;
                }
                else
                {
                    Console.WriteLine("Argument {0}:\"{1}\" is not recognized", nextarg, arg);
                    Usage();
                }
            }

            try
            {
                // Create Reader object, connecting to physical device.
                // Wrap reader in a "using" block to get automatic
                // reader shutdown (using IDisposable interface).
                using (Reader r = Reader.Create(args[0]))
                {
                    //Uncomment this line to add default transport listener.
                    //r.Transport += r.SimpleTransportListener;

                    r.Connect();
                    if (Reader.Region.UNSPEC == (Reader.Region)r.ParamGet("/reader/region/id"))
                    {
                        Reader.Region[] supportedRegions = (Reader.Region[])r.ParamGet("/reader/region/supportedRegions");
                        if (supportedRegions.Length < 1)
                        {
                            throw new FAULT_INVALID_REGION_Exception();
                        }
                        r.ParamSet("/reader/region/id", supportedRegions[0]);
                    }
                    string model = r.ParamGet("/reader/version/model").ToString();
                    Boolean checkPort = (Boolean)r.ParamGet("/reader/antenna/checkPort");
                    String swVersion = (String)r.ParamGet("/reader/version/software");
                    if ((model.Equals("M6e Micro") || model.Equals("M6e Nano") ||
                        (model.Equals("Sargas") && (swVersion.StartsWith("5.1"))))
                        && (false == checkPort) && antennaList == null)
                    {
                        Console.WriteLine("Module doesn't has antenna detection support please provide antenna list");
                        Usage();
                    }
                    // Create a simplereadplan which uses the antenna list created above
                    SimpleReadPlan plan = new SimpleReadPlan(antennaList, TagProtocol.GEN2,null,null,1000);
                    // Set the created readplan
                    r.ParamSet("/reader/read/plan", plan);

                    // Create and add tag listener
                    PrintNewListener rl = new PrintNewListener();
                    r.TagRead += rl.TagRead;

                    // Create and add read exception listener
                    r.ReadException += new EventHandler<ReaderExceptionEventArgs>(r_ReadException);
                    // Search for tags in the background
                    r.StartReading();
                    Thread.Sleep(10000);
                    r.StopReading();

                    r.TagRead -= rl.TagRead;
                }
            }
            catch (ReaderException re)
            {
                Console.WriteLine("Error: " + re.Message);
                Console.Out.Flush();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }

        static void r_ReadException(object sender, ReaderExceptionEventArgs e)
        {
            Console.WriteLine("Error: " + e.ReaderException.Message);
        }

        #region ParseAntennaList

        private static int[] ParseAntennaList(IList<string> args, int argPosition)
        {
            int[] antennaList = null;
            try
            {
                string str = args[argPosition + 1];
                antennaList = Array.ConvertAll<string, int>(str.Split(','), int.Parse);
                if (antennaList.Length == 0)
                {
                    antennaList = null;
                }
            }
            catch (ArgumentOutOfRangeException)
            {
                Console.WriteLine("Missing argument after args[{0:d}] \"{1}\"", argPosition, args[argPosition]);
                Usage();
            }
            catch (Exception ex)
            {
                Console.WriteLine("{0}\"{1}\"", ex.Message, args[argPosition + 1]);
                Usage();
            }
            return antennaList;
        }

        #endregion

    }

    class PrintNewListener
    {
        Hashtable SeenTags = new Hashtable();

        public void TagRead(Object sender, TagReadDataEventArgs e)
        {
            lock (SeenTags.SyncRoot)
            {
                try
                {
                    TagData t = e.TagReadData.Tag;
                    string epc = t.EpcString;
                    if (!SeenTags.ContainsKey(epc))
                    {
                        Console.WriteLine("New tag: " + t.ToString());
                        SeenTags.Add(epc, null);
                    }
                }
                catch (ArgumentException ex)
                {
                    Console.WriteLine("EPC already added");
                }
            }
        }
    }
}
