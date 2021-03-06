############## errror code

# killed
EC_Kill = 100

# transfer timeout
EC_Transfer = 101

# expire
EC_Expire = 102

# aborted
EC_Aborted = 103

# wait timeout
EC_WaitTimeout = 104

# reassigned by rebrokeage 
EC_Reassigned = 105

# reassigned by server-side retry
EC_Retried = 106

# retried by pilot
EC_PilotRetried = 107

# lost file (=dataservice.ErrorCode.EC_LostFile)
EC_LostFile = 110

# retried for event service
EC_EventServiceRetried = 111

# merge for event service
EC_EventServiceMerge = 112

# merge job failed
EC_MergeFailed = 113

# max attempt reached for Event Service
EC_EventServiceMaxAttempt = 114

# do nothing since other consumers are still running
EC_EventServiceWaitOthers = 115

# killed since unused and unnecessary any more 
EC_EventServiceUnused = 116

# didn't process any events on WN
EC_EventServiceUnprocessed = 117



# file not found
class EC_NotFound:
    pass

# file relocated
class EC_Redirect:
    def __init__(self,url):
        self.url = url
