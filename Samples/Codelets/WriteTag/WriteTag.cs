//Uncomment this to enable filter
//#define ENABLE_FILTER
//Uncomment this to enable readafterwrite functionality
//#define ENABLE_READ_AFTER_WRITE 

using System;
using System.Collections.Generic;
using System.Text;

// Reference the API
using ThingMagic;

namespace WriteTag
{
    /// <summary>
    /// Sample program that writes an EPC to a tag and demonstrates the functionality of read after write
    /// </summary>
    class WriteTag
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
            TagFilter filter = null;
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
                    //Use first antenna for operation
                    if (antennaList != null)
                        r.ParamSet("/reader/tagop/antenna", antennaList[0]);

                    // This select filter matches all Gen2 tags where bits 32-48 of the EPC are 0x0123 
#if ENABLE_FILTER
                    filter = new Gen2.Select(false, Gen2.Bank.EPC, 32, 16, new byte[] { 0x01, 0x23});
#endif

                    Gen2.TagData epc = new Gen2.TagData(new byte[] {
                        0x01, 0x23, 0x45, 0x67, 0x89, 0xAB,
                        0xCD, 0xEF, 0x01, 0x23, 0x45, 0x67,
                    });
                    Gen2.WriteTag tagop = new Gen2.WriteTag(epc);
                    r.ExecuteTagOp(tagop, filter);

                    // Reads data from a tag memory bank after writing data to the requested memory bank without powering down of tag
#if ENABLE_READ_AFTER_WRITE
                    {
                        //create a tagopList with write tagop followed by read tagop
                        TagOpList tagopList = new TagOpList();
                        byte wordCount;
                        ushort[] readData;

                        //Write one word of data to USER memory and read back 8 words from EPC memory using WriteData and ReadData
                        {
                            ushort[] writeData = { 0x1234 };
                            wordCount = 8;
                            Gen2.WriteData wData = new Gen2.WriteData(Gen2.Bank.USER, 2, writeData);
                            Gen2.ReadData rData = new Gen2.ReadData(Gen2.Bank.EPC, 0, wordCount);

                            // assemble tagops into list
                            tagopList.list.Add(wData);
                            tagopList.list.Add(rData);

                            // call executeTagOp with list of tagops
                            readData = (ushort[])r.ExecuteTagOp(tagopList, filter);
                            Console.WriteLine("ReadData: ");
                            foreach (ushort word in readData)
                            {
                                Console.Write(" {0:X4}", word);
                            }
                            Console.WriteLine("\n");
                        }

                        //clearing the list for next operation
                        tagopList.list.Clear();

                        //Write 12 bytes(6 words) of EPC and read back 8 words from EPC memory using WriteTag and ReadData
                        {
                            Gen2.TagData epc1 = new Gen2.TagData(new byte[] {
                                 0x11, 0x22, 0x33, 0x44, 0x55, 0x66,
                                 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc,
                            });
                            wordCount = 8;
                            Gen2.WriteTag wtag = new Gen2.WriteTag(epc1);
                            Gen2.ReadData rData = new Gen2.ReadData(Gen2.Bank.EPC, 0, wordCount);

                            // assemble tagops into list
                            tagopList.list.Add(wtag);
                            tagopList.list.Add(rData);

                            // call executeTagOp with list of tagops
                            readData = (ushort[])r.ExecuteTagOp(tagopList, filter);
                            Console.WriteLine("ReadData: ");
                            foreach (ushort word in readData)
                            {
                                Console.Write(" {0:X4}", word);
                            }
                            Console.WriteLine("\n");
                        }
                    }
#endif
                }
            }
            catch (ReaderException re)
            {
                Console.WriteLine("Error: " + re.Message);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
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
}
