from conan.packager import ConanMultiPackager
import os

visual_versions =  os.getenv("CONAN_VISUAL_VERSIONS", "12,14")
visual_versions = list(filter(None, visual_versions.split(",")))

if __name__ == "__main__":
    builder = ConanMultiPackager(username="demo")
    builder.add_common_builds(visual_versions = visual_versions)
    builder.run()