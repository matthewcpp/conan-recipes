from conans import ConanFile, CMake, tools


class TinysoundfontConan(ConanFile):
    name = "TinySoundFont"
    version = "21c07c0"
    license = "MIT"
    url = "https://github.com/schellingb/TinySoundFont"
    description = "SoundFont2 synthesizer library in a single C/C++ file "
    topics = ("SoundFont2")
    no_copy_source = True
    build_policy = "always"
    git_revision = "21c07c0bcd702e7adf3db349ac926914b98d17ce"

    def source(self):
        tools.download("https://raw.githubusercontent.com/schellingb/TinySoundFont/{}/tsf.h".format(self.git_revision), "tsf.h")

    def package(self):
        self.copy("tsf.h", dst="include")

    def package_id(self):
        self.info.header_only()


