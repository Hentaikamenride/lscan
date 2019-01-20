# Copyright (C) 2018 - This notice is to be included in all relevant source files.
# "Brandon Goldbeck" <bpg@pdx.edu>
# “Anthony Namba” <anamba@pdx.edu>
# “Brandon Le” <lebran@pdx.edu>
# “Ann Peake” <peakean@pdx.edu>
# “Sohan Tamang” <sohan@pdx.edu>
# “An Huynh” <an35@pdx.edu>
# “Theron Anderson” <atheron@pdx.edu>
# This software is licensed under the MIT License. See LICENSE file for the full text.
import wx
from src.ui.iui_behavior import IUIBehavior
from src.ui.application_state import ApplicationState
from src.ui.user_event import UserEvent
from pathlib import Path

class MetadataPanel(wx.Panel, IUIBehavior):
    """This class contains the wx widgets for control over metadata information in the
    program. These widgets may include, but not limited to author, license, stl file input,
    and ldraw file output.
    """
    text_ctrl_size = (400, 20)
    max_path_length = 256
    big_button = (120, 25)
    small_button_size = (30, 25)
    panel_size = (1024, 100)
    label_size = (150, 25)

    def __init__(self, parent):
        """Default constructor for MainPanel class.
        """
        wx.Panel.__init__(self, parent, size=self.panel_size, style=wx.BORDER_SUNKEN)
        self.parent = parent
        self.browse_stl_button = None
        self.help_button = None
        self.about_button = None
        self.browse_stl_button = None
        self.author_text = None
        self.license_text = None
        self._build_gui()
        self.parent.Layout()

    def _build_gui(self):
        """Initializing input, output, process control, and log panel elements
        :return:
        """
        self.SetBackgroundColour("#777fea")

        # Input
        path_name_static_text = wx.StaticText(
            self,
            label="Path to Input STL File",
            size=self.label_size,
            style=wx.ALIGN_RIGHT)

        # Stl input.
        stl_path_name_text = wx.TextCtrl(self, size=self.text_ctrl_size)
        stl_path_name_text.SetMaxLength(self.max_path_length)

        self.browse_stl_button = wx.Button(self, label="Browse STL", size=self.big_button)

        # Help / About.
        self.help_button = wx.Button(self, label="?", size=self.small_button_size)
        self.about_button = wx.Button(self, label="i", size=self.small_button_size)

        # Output path selection.
        path_part_static_text = wx.StaticText(self, label="Part Name", size=self.label_size, style=wx.ALIGN_RIGHT)
        ldraw_name_text = wx.TextCtrl(self, size=self.text_ctrl_size)
        ldraw_name_text.SetMaxLength(self.max_path_length)

        self.browse_output_button = wx.Button(self, label="Browse Output", size=self.big_button)

        # Author
        author_static_text = wx.StaticText(self, label="Author", size=self.label_size, style=wx.ALIGN_RIGHT)
        self.author_text = wx.TextCtrl(self, size=self.text_ctrl_size)
        self.author_text.SetMaxLength(self.max_path_length)

        # License information.
        license_static_text = wx.StaticText(self, label="License", size=self.label_size, style=wx.ALIGN_RIGHT)
        self.license_text = wx.TextCtrl(self, size=self.text_ctrl_size)
        self.license_text.SetMaxLength(self.max_path_length)

        # Create the layout.
        horizontal_input = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_output = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_author = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_license = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_input.Add(path_name_static_text, 0, wx.ALIGN_CENTER)
        horizontal_input.AddSpacer(5)
        horizontal_input.Add(stl_path_name_text, 0, wx.ALIGN_CENTER)
        horizontal_input.AddSpacer(5)
        horizontal_input.Add(self.browse_stl_button, 0, wx.ALIGN_CENTER)
        horizontal_input.AddSpacer(5)
        horizontal_input.Add(self.help_button, 0, wx.ALIGN_CENTER)
        horizontal_input.AddSpacer(5)
        horizontal_input.Add(self.about_button, 0, wx.ALIGN_CENTER)

        horizontal_output.Add(path_part_static_text, 0, wx.ALIGN_LEFT)
        horizontal_output.AddSpacer(5)
        horizontal_output.Add(ldraw_name_text, 0, wx.ALIGN_LEFT)
        horizontal_output.AddSpacer(5)
        horizontal_output.Add(self.browse_output_button, 0, wx.ALIGN_LEFT)

        horizontal_author.Add(author_static_text, 0, wx.ALIGN_LEFT)
        horizontal_author.AddSpacer(5)
        horizontal_author.Add(self.author_text, 0, wx.ALIGN_LEFT)

        horizontal_license.Add(license_static_text, 0, wx.ALIGN_LEFT)
        horizontal_license.AddSpacer(5)
        horizontal_license.Add(self.license_text, 0, wx.ALIGN_LEFT)

        vertical_layout = wx.BoxSizer(wx.VERTICAL)
        vertical_layout.Add(horizontal_input, 0, wx.ALIGN_LEFT)
        vertical_layout.Add(horizontal_output, 0, wx.ALIGN_LEFT)
        vertical_layout.Add(horizontal_author, 0, wx.ALIGN_LEFT)
        vertical_layout.Add(horizontal_license, 0, wx.ALIGN_LEFT)

        horizontal_split = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_split.AddSpacer(150)
        horizontal_split.Add(vertical_layout, 0, wx.ALIGN_LEFT)

        self.SetSizer(horizontal_split)

        # Register events.
        self.Bind(wx.EVT_BUTTON, self.about, self.about_button)
        self.Bind(wx.EVT_BUTTON, self.browse_output, self.browse_output_button)
        self.Bind(wx.EVT_BUTTON, self.help, self.help_button)
        self.Bind(wx.EVT_BUTTON, self.browse_input, self.browse_stl_button)

    def help(self, event):
        """Presents program limitations, common troubleshooting steps, and steps to update LDraw parts library.
        :param event:
        :return:
        """
        wx.MessageBox("""
            Program Limitations
            TEXT
            Troubleshooting
            TEXT
            How to update LDraw Parts Library
            TEXT""", "Help info", wx.OK | wx.ICON_QUESTION)

    def about(self, event):
        """Presents program name, program version, copyright information, licensing information, and authors to user.
        :param event:
        :return:
        """
        wx.MessageBox("""
            LScan
            Version 1.0
            Copyright (C) 2018 - This notice is to be included in all relevant source files.

            This software is licensed under the MIT License. See LICENSE file for the full text.

            Authors
            "Brandon Goldbeck" <bpg@pdx.edu>
            “Anthony Namba” <anamba@pdx.edu>
            “Brandon Le” <lebran@pdx.edu>
            “Ann Peake” <peakean@pdx.edu>
            “Sohan Tamang” <sohan@pdx.edu>
            “An Huynh” <an35@pdx.edu>
            “Theron Anderson” <atheron@pdx.edu>""", "About LScan", wx.OK | wx.ICON_INFORMATION)

    def browse_input(self, event):
        """Browse for a valid STL input file.
        :param event:
        :return:
        """
        stl_wildcard = "*.stl"
        print(Path.cwd())
        dialog = wx.FileDialog(self, "Choose a STL file", defaultDir="", wildcard=stl_wildcard, style=wx.FD_OPEN
                               | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_OK:
            filename = dialog.GetPath()
            # Check for file existing
            # If valid, pass to worker thread who will check data
            print(filename)
            #try:
            #    with open(filename, "r", encoding="utf-8") as file:
            #        stl_data = file.read()
            #        print(stl_data)
            #except IOError:
            #    print("IO ERROR!")
            #stl_data = self.get_file_text(dialog.GetCurrentlySelectedFilename)
            #print(stl_data)
        dialog.Destroy()

    def get_file_text(self, filepath):
        enc = "utf-8"
        try:
            with open(str(filepath), "r", encoding=enc) as file:
                text = file.read()

        except PermissionError as perr:
            # Print to Log !!!!
            print(perr)
            raise
        except FileNotFoundError as ferr:
            # Print to Log !!!!
            print(ferr)
            raise
        else:
            return text

    def browse_output(self, event):
        """Browse for a valid DAT output file
        :param event:
        :return:
        """
        pass

    def on_state_changed(self, new_state: ApplicationState):
        """A state change was passed to the MetadataPanel.

        :param new_state: The recorded ApplicationState.
        :return: None
        """
        pass

    def on_event(self, event: UserEvent):
        """A user event was passed to the MetadataPanel.

        :param event: The recorded UserEvent.
        :return: None
        """
        pass

    def create_settings(self):
        """Generate inital settings file based on current working directory.
        """
        pass

    def save_settings(self):
        """Save changes to user settings file.
        """
        # Determine changes to settings file
        # Write out changes to
        pass

    def read_settings(self):
        """Read the settings file."""
        pass

    def write_settings(self):
        """Write to the settings file."""
        pass
