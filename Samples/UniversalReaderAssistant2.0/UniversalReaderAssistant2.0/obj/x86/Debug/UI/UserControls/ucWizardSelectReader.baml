   M S B A M L   `   `   `  ����  UniversalReaderAssistant*    $ThingMagic.URA2.ucWizardSelectReader   5      R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      @d2http://schemas.microsoft.com/expression/blend/2008     5      X TXceed.Wpf.Toolkit, Version=2.5.0.0, Culture=neutral, PublicKeyToken=3e4669d2f30244f44xctk)http://schemas.xceed.com/wpf/xaml/toolkit  5        � 	Resources  5	       �� MergedDictionaries �� Source�� 5
   
    5      �� 5      $, &../../Stylesheet/WizardPagesTheme.xaml?�6%   %    5      .��5      � $��Center=�6    � RowDefinitions 5   
   �� 5      $
��Auto �6   �� 5      $
��Auto �6   �� 5      $
��Auto �6   �� 5      $
��Auto �6    � ColumnDefinitions 5   
   �� 5      $��* �6   �� 5      $��3* �6   .+�5   
   �� $��0��6   $��0��6   $��5q�6-   $��2��68   $��Center=�6L   $��DemiBold"�6i   $��Please Select a Reader��6   �� 5   
   $��1��6   $��0��6   $��5q�6-   $��DemiBold"�68   $��Right=�6N   $��Center=�6j   $��Reader Type :��6�   �� 5   
   $��1��6   $��1��6"    �� Orientation$ 
Horizontal=�62   .+�5      	� $��5q�6   $��Center=�6%   $��Serial Reader��6@    d� 	IsChecked 6X   �� *IsSerialReader+��6}   �� *ReaderTypeCheckedCommand+	� 5       $��5q�6   $��Center=�6%   $��Network Reader��6@    6Y   �� *IsNetworkReader+��6   �� *ReaderTypeCheckedCommand+	� 5!      -   5         	�Name$ rbtnAddCustomReader��5!      $��5q�67   $��Center=�6B   $��Custom Transport Reader��6]    6   �� *IsAddCustomReader+��6�   �� *ReaderTypeCheckedCommand+5"      �� 5$   
   $��2��6   $��0��6   $��5q�6-   $��DemiBold"�68   $��Right=�6N   $��Center=�6j   $��Reader Name :��6�   �� 5&   
   $��2��6   $��1��6"   $ 
Horizontal=�62   .+�5'      )  #Xceed.Wpf.Toolkit.WatermarkComboBox  -   5          Name$ cbxReaderList��5'   %   $��5q�6>   $	��250��6I   $
��Left=�6U   	 �� 
IsEditable	 . $��Center=�6'  ��6p   �� *
ReaderList+
 �� UpdateSourceTrigger$
 PropertyChanged=� �� Mode$ TwoWay=� �� SelectedItem 6�   �� *ReaderListSelectedItem+ �� Text 6  �� *ReaderListText+  5(       �� 
TargetType �� Triggers �� Binding �� Value �� Property �� Value �� ElementName �� Path��%Q  '        �� 5)      "  6    5+      �� 5,       6*   �� *IsNetworkReader+ True6N   .a�5-   "   ��  �@ 	Watermark$  ex. 10.2.0.103��6>   5.      �� 5/       6*   �� *IsSerialReader+ True6M   .a�50   "   ��  �@ 	Watermark$ 
 ex. COM47��6>   51      �� 52       6*   �� $ rbtnAddCustomReader��$ 	IsChecked� True6n   .a�53   "   ��  � y�$ 	Collapsed=�6?   54      �� 55       6*   �� $ rbtnAddCustomReader��$ 	IsChecked�	 False6n   .a�56   "   ��  � y�$ Visible=�6?   57      5=      5>      5?      (  "Xceed.Wpf.Toolkit.WatermarkTextBox  5O      -   5          Name$ 	txtHostIP��5O   H      	Watermark$  ex. 172.16.16.106:5000��6$   $��5q�6[   $	��250��6f   $
��Left=�6r   ��6�   �� *HostAddress+$
 PropertyChanged=�.��6�   ��5P      �� 5Q      " ��6    5R      �� 5S       6*   �� $ rbtnAddCustomReader��$ 	IsChecked� True6n   .a�5T   "   ��  � y�$ Visible=�6?   5U      �� 5V       6*   �� $ rbtnAddCustomReader��$ 	IsChecked�	 False6n   .a�5W   "   ��  � y�$ 	Collapsed=�6?   5X      5Z      .��5[   /   5\      �� 5m      -   5         ��Name$ cbxAddManual��5m      $��5q�6-   $��Center=�68   $��Add Name Manually��6|   $y�	Collapsed=�6�    6S   �� *IsAddManualChecked+��6�   �� *ReaderTypeCheckedCommand+6�   5o      ]� 5t   
   $��3��6   $��1��6!   .+�5u      �� $��3��6   $��1��6#      ButtonTheme#��[  63   $	��120��6X   $��30��6d   ���	#FF25A0DA$
��Left=�6�   $
��Left=�6�   $��5q�6�   $��Refresh��6�   ��6�   �� *ReaderTypeCheckedCommand+5w      5z      5{      