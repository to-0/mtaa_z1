import time
class CallLogger:
    def __init__(self, f):
        self.cancel = False
        self.log_file = f
        self.call_in_process = False
        self.active_calls = {}
        self.unack_calls = {}

    def invitel(self, origin, destination):
        # ak ten call uz nie je aktivny nahodou
        if self.active_calls.get(origin) is None and (self.active_calls.get(destination) is None or self.active_calls.get(destination) != origin):
            self.log_file.write("INVITE from " + origin +" to "+ destination+ " at "+time.strftime("(%H:%M:%S %d.%m.%Y)", time.localtime())+ "\n")
            self.unack_calls[origin] = destination


    def ack(self, origin, destination):
        # nedostal som cancel cize to zdvihol
        if self.cancel is not True and self.active_calls.get(origin) is None and self.unack_calls.get(origin) is not None:
            self.log_file.write("Call acknowledged at "+time.strftime("%H:%M:%S %d.%m.%Y", time.localtime())+ "\n")
            self.active_calls[origin] = destination
            self.call_in_process = True

    def cancel_log(self, origin):
        if self.unack_calls.get(origin) is not None:
            self.log_file.write("Call cancelled at " + time.strftime("%H:%M:%S %d.%m.%Y", time.localtime()) + "\n")
            self.unack_calls.pop(origin)

    def bye(self, origin):
        self.log_file.write("Call finished at " + time.strftime("%H:%M:%S %d.%m.%Y", time.localtime())+"\n")
        self.call_in_process = False
        if self.active_calls.get(origin) is not None:
            self.active_calls.pop(origin)


