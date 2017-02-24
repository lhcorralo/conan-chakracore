from conans import ConanFile, CMake
import os

# This easily allows to copy the package in other user or channel
username = os.getenv("CONAN_USERNAME", "lhcorralo")
channel = os.getenv("CONAN_CHANNEL", "testing")

class caresReuseConan(ConanFile):
    settings = {"os": ["Windows"],
		"compiler": {"Visual Studio": {"version": ["12", "14"], "runtime" : None }},
		"arch": None,
		"build_type": None}
    requires = "ChakraCore/1.4.1@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        # Copy shared libraries
        self.copy(pattern="*.dll", dst="bin", src="bin")

    def test(self):
        # equal to ./bin/greet, but portable win: .\bin\greet
        self.run(os.sep.join([".","bin", "HelloWorld.exe"]))