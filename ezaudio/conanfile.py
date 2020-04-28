from conans import ConanFile, CMake, tools


class EzaudioConan(ConanFile):
    name = "ezaudio"
    version = "d743d34"
    license = "MIT"
    url = "https://github.com/matthewcpp/ezaudio"
    description = "https://github.com/matthewcpp/ezaudio"
    topics = ("wasapi", "coreaudio")
    no_copy_source = True
    git_revision = "d743d34423f33f4ac8f9c62e72af00b02c63827e"
    build_policy = "always"

    def source(self):
        self.run("git clone https://github.com/matthewcpp/ezaudio.git ")
        with tools.chdir("./ezaudio"):
            self.run("git checkout {}".format(self.git_revision))

    def package(self):
        combine_script = self.source_folder + "/ezaudio/scripts/make_header_only.py"
        self.run("python {} ezaudio.h".format(combine_script))
        self.copy("ezaudio.h", dst="include/ezaudio")

    def package_id(self):
        self.info.header_only()


