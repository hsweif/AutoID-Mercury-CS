   M S B A M L   `   `   `  ����  UniversalReaderAssistant#    ThingMagic.URA2.ucUntraceable   5      R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      @d2http://schemas.microsoft.com/expression/blend/2008     5      .��5      �� -   5        $��spUntraceable��5   4     �� Orientation$  Vertical=�6   $��10q�6(   {�.  $	��600��6[   $
��Left=�6g    � 	Resources 5	   
      boolToVisible��%   &	        �� 5
      6+   5      .+�5   
   �� $��5q�6   $b��\ Note : Untraceable Operation supports only GEN2 Tags. Rest of the protocols will be ignored��6   6�   �� 5   
   -   5        $��tagUntraceable��5      
���������5      �� 5      $
��Bold"�6   Tag to Read/Write6A   .��5      �� -   5        $��grid1��5      $��5q�6&   $  Vertical=�61   .+�5      �� $  
Horizontal=�6   .+�5      �� $  Vertical=�6!   .+�5      	� -   5        $��rbFirstTagUntraceableTb��5   �   $��First tag to respond ��6P    	� 	GroupName$ UntraceableTab��6p    d� 	IsChecked$
 TrueY�6�   $��3q�6�   6�   	� 5      -   5        $ ��rbSelectedTagUntraceableTb��5   �    ^� ShowOnDisabled .  � ToolTip$: 4Go to Tag Results tab and right-click on a data cell��6K   $&�� Tag selected in Tag Results page��6�   $ UntraceableTab��6�   $��3q�6�   {�.  6�   5      �� 5      -   5        $��btnRead��5   >   $
��Read��6   $��30,3,3,3q�6,   $��Center=�6M   $��75��6h   6s   5      � 5      -   5        $��gdTagSelectionCriteria��5      .+�5      �� $  Vertical=�6!   $��3q�68   .+�5      �� -   5        $��lblSelectFilter��5   +   $��3q�6    $
��Left=�6B   $��Showing tag :��6^   �� 5      -	   5        $��lblUntraceableTagError��5   V   $��3q�6    $��Error��6+   $
��Left=�6;   $��Center=�6t   $y�	Collapsed=�6�   ���	#FFF60909 J� OpacityMask �	#FFFA00006�   5      5      �� 5      -
   5        $��txtEpc��5   5   $��23��6   $��3q�6*   $	��Top=�6C   $y�	Collapsed=�6[   $��Right=�6r   $��28��6�   �� 5       -   5        $��txtData��5    P   $��23��6   $
��Left=�6*   $��3q�6E   $	��Top=�6_   $y�	Collapsed=�6w   $��28��6�   5!      5"      �� 5$   
   -   5        $��spUntraceableFields��5$      $
��Auto��60   $
��Auto��6=   
�������$��	0,10,0,20q�6^   .+�5%      �� $  
Horizontal=�6   $��10q�62   .+�5&      �� -   5        $��lblAccesspwd��5&   4   $��Access Password :��6   $
��Auto��6H   $
��Auto��6V   $��Center=�6c   �� 5'      -   5        $��txtbxAccesspaasword��5'   �    �� 
CaretBrush
 �   ����	#0A000000$�� ��6E   $��80��6�   $��10,0,0,0q�6�   $��25��6�    �� 	MaxLength$ 8��6�   $��Center=�6  5(      �� 5*      -   5        $	��Epc��5*      $��0q�6"   $
��Auto��66   ��5+      �� 5,      $
��Bold"�6    EPC67   .��5.      �� -   5        $��grdEpc��5.   +   $
��Auto��6   $
��Auto��69   $  Vertical=�6F   .+�5/      	� -   5        $��rdBtnShowEntireEpc��5/   <   $��Show Entire EPC��6"   $ 
epcUntrace��6V   $��2q�6m   $
 TrueY�6x   6�   �� 50      $  
Horizontal=�6!   $
��Auto��6:   $
��Auto��6H   $��2q�6U   .+�51      	� -   5        $��rdBtnShowSpecificEpc��51   &   $��Show EPC to length : ��6C   $ 
epcUntrace��6c   $��Center=�6�   �� 52      -   5        $��txtbxEpcLen��52   "   {�.  $��25��6G   $ 2��6R   $��Center=�6�   6�   �� 53      $��Words��6    $
��Auto��60   $��Center=�6>   54      55      56      �� 58      -   5        $	��TID��58      $��0q�6"   $
��Auto��66   ��59      �� 5:      $
��Bold"�6    TID67   .��5<      �� -   5        $��grdTid��5<   +   $
��Auto��6   $
��Auto��69   $  Vertical=�6F   .+�5=      	� -   5        $��rdbtnShowAllTid��5=   "   $��Show All��69   $ 
tidUntrace��6L   $��2q�6c   $
 TrueY�6n   6   	� 5>      -   5        $��rdbtnShowTaginfo��5>   "   $��Show Tag Info Only��6:   $ 
tidUntrace��6W   $��2q�6n   6y   	� 5?      -   5        $��rdbtnShowNone��5?   "   $��	Show None��67   $ 
tidUntrace��6K   $��2q�6b   6m   5@      5A      �� 5C      -   5        $
��User��5C      $��0q�6#   $
��Auto��67   ��5D      �� 5E      $
��Bold"�6    USER68   .��5G      �� -   5        $��grdUser��5G   +   $
��Auto��6   $
��Auto��6:   $��0q�6G   .+�5H      	� -   5        $��rdbtnShowUserMem��5H   "   $��Show All��6:   $ userUntrace��6M   $��2q�6e   $
 TrueY�6p   6�   	� 5I      -   5        $��rdbtnHideUserMem��5I   "   $��	Show None��6:   $ userUntrace��6N   $��2q�6f   6q   5J      5K      �� 5M      -   5        $��btmWriteToTag��5M   C   $��Write to Tag��6   $��5q�6,   $��25��67   $��1q�6X   $	��100��6�   $��Center=�6�   6�   5N      5O      5P      