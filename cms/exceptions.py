class CMSError(Exception):
    pass


class DevelopError(CMSError):
    def __init__(self, code=None, params=None):
        super().__init__(
            "Develop restart task failed",
            500,
            params
        )


class BuildIsAlreadyRunningError(CMSError):
    def __init__(self, code=None, params=None):
        super().__init__(
            "Build is already running",
            500,
            params
        )
