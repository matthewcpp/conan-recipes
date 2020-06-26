from conans import ConanFile, CMake, tools


class EzaudioConan(ConanFile):
    name = "ezmidi"
    version = "565114c"
    license = "MIT"
    url = "https://github.com/matthewcpp/ezmidi"
    description = "https://github.com/matthewcpp/ezmidi"
    topics = ("midi", "windowsmm", "coreaudio", "alsa")
    no_copy_source = True
    git_revision = "565114ce2037b6e97cdb31db7189f0504c47fadf"
    build_policy = "always"

    def source(self):
        self.run("git clone https://github.com/matthewcpp/ezmidi.git ")
        with tools.chdir("./ezmidi"):
            self.run("git checkout {}".format(self.git_revision))

    def package(self):
        combine_script = self.source_folder + "/ezmidi/scripts/make_header_only.py"
        self.run("python {} ezmidi.h".format(combine_script))
        self.copy("ezmidi.h", dst="include/ezmidi")

    def package_id(self):
        self.info.header_only()


