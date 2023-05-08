from tool.app.appConsturctor import AppConstructor
from tool.app.argParser import ArgParser


if __name__ == "__main__":
    AppConstructor(
        parser=ArgParser().name
    )

