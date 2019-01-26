# Copyright (C) 2018
# This notice is to be included in all relevant source files.
# "Brandon Goldbeck" <bpg@pdx.edu>
# “Anthony Namba” <anamba@pdx.edu>
# “Brandon Le” <lebran@pdx.edu>
# “Ann Peake” <peakean@pdx.edu>
# “Sohan Tamang” <sohan@pdx.edu>
# “An Huynh” <an35@pdx.edu>
# “Theron Anderson” <atheron@pdx.edu>
# This software is licensed under the MIT License.
# See LICENSE file for the full text.
import datetime
from src.log_messages.log_type import LogType


class LogMessage:
    """Data class for a LogMessage. A log message contains a message, message type, and timestamp
    for the message.
    """

    def __init__(self, message_type: LogType, message: str):
        """Constructor for the LogMessage class.
        """
        self.timestamp = datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p")
        self.message = message
        self.message_type = message_type

    def get_message(self):
        """Get the message data.

        :return: The message data as a str object
        """
        return self.message

    def get_message_type(self):
        """Get the type of message from this log message.

        :return: The LogType stored with the log message.
        """
        return self.message_type

    def get_timestamp(self):
        """Get the timestamp this message was created. See http://strftime.org/ for details.

        :return: The time stamp from the datetime python module.
        """
        return self.timestamp

