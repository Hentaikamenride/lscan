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
import wx.richtext as rt
from src.ui.application_state import ApplicationState
from src.ui.user_event import UserEvent
from src.ui.user_event_type import UserEventType
from src.ui.iui_behavior import IUIBehavior
from src.log_messages.log_message import LogMessage
from src.log_messages.log_type import LogType
from src.ui.ui_style import *


class LogPanel(wx.Panel, IUIBehavior):
    """This panel controls the behavior for the output log panel that will display
    running information to the user about the programs progress while running
    various algorithms.
    """
    _log_file_path = "log.txt"

    def __init__(self, parent):
        """Default constructor for MainPanel class.

        :param parent: The parent wx object for this panel.
        """
        wx.Panel.__init__(self, parent, size=UI_style.log_panel_size, style=UI_style.log_border)
        self.parent = parent
        self.save_log_button = None
        self.log_text_ctrl = None
        self._build_gui()

    def _build_gui(self):
        """Create the necessary wx objects for the functional purposes of this output
        log panel.

        :return: None
        """
        # Build the wx control objects.
        self.SetBackgroundColour(UI_style.log_background_color)
        style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_RICH

        self.save_log_button = wx.Button(self, label="Save Log", size=UI_style.log_big_button)
        self.save_log_button.SetBackgroundColour(UI_style.button_background)
        self.save_log_button.SetForegroundColour(UI_style.button_text)
        self.log_text_ctrl = rt.RichTextCtrl(self, size=UI_style.log_output_size, style=style)
        self.log_text_ctrl.SetBackgroundColour(wx.Colour(UI_style.log_text_background_color))

        self.Bind(wx.EVT_BUTTON, self.save_log, self.save_log_button)

        # Build the layout.
        horizontal_layout = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_layout.Add(self.log_text_ctrl, 0, flag=wx.ALIGN_LEFT)
        horizontal_layout.AddSpacer(5)
        horizontal_layout.Add(self.save_log_button, 0, wx.ALIGN_RIGHT)

        self.SetSizer(horizontal_layout)
        self.Show()

    def save_log(self):
        """Save the feedback log to a file.

        :return: None
        """
        try:
            log_file = open(self._log_file_path, mode="w")
            log_file.write(self.log_text_ctrl.GetValue())
            log_file.close()
        except IOError:
            pass
        finally:
            pass

    def clear_log(self):
        """Clears the log.

        :return:
        """
        self.log_text_ctrl.Clear()

    def on_state_changed(self, new_state: ApplicationState):
        """A state change was passed to the LogPanel.

        :param new_state: The recorded ApplicationState.
        :return: None
        """
        if new_state == ApplicationState.STARTUP:
            self.save_log_button.Disable()

        self.handle_log_message(
            LogMessage(LogType.DEBUG, "State changed to: " + str(new_state)))

    def on_event(self, event: UserEvent):
        """A user event was passed to the LogPanel.

        :param event: The recorded UserEvent.
        :return: None
        """
        if event is not None:
            if event.get_log_message() is not None:
                self.handle_log_message(event.get_log_message())

    def handle_log_message(self, log_message: LogMessage):
        """Take apart the log message and display it to the log. Different types of messages
        will have different colors.
            -INFO: White
            -WARNING: Yellow
            -ERROR: Red
            -DEBUG: Blue

        :param log_message: The LogMessage that will be displayed on the log.
        :return: None
        """
        if log_message is not None:
            message = log_message.get_message()
            timestamp = log_message.get_timestamp()
            color = log_message.get_log_message_color()
            log_type = log_message.get_message_type()

            if log_type == LogType.DEBUG and __debug__ or log_type != LogType.DEBUG:
                self.log_text_ctrl.BeginFontSize(UI_style.log_font_size)
                self.log_text_ctrl.BeginTextColour(UI_style.log_default_text_color)
                self.log_text_ctrl.WriteText(timestamp + ": ")
                self.log_text_ctrl.BeginTextColour(wx.Colour(color))
                self.log_text_ctrl.WriteText(message + "\n")
                self.log_text_ctrl.EndFontSize()

                # Scrolls down to show last line added
                self.log_text_ctrl.ShowPosition(self.log_text_ctrl.GetLastPosition())
