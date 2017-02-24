find_path(CHAKRACORE_INCLUDE_DIR NAMES ChakraCore.h PATHS ${CONAN_INCLUDE_DIRS_CHAKRACORE})
MESSAGE("** CONAN_LIBS_CHAKRACORE:  ${CONAN_LIBS_CHAKRACORE}")
MESSAGE("** CONAN_LIB_DIRS_CHAKRACORE:  ${CONAN_LIB_DIRS_CHAKRACORE}")
find_library(CHAKRACORE_LIBRARY NAMES ${CONAN_LIBS_CHAKRACORE} PATHS ${CONAN_LIB_DIRS_CHAKRACORE})

MESSAGE("** CHAKRACORE ALREADY FOUND BY CONAN!")
SET(CHAKRACORE_FOUND TRUE)
MESSAGE("** FOUND CHAKRACORE INCLUDE:  ${CHAKRACORE_INCLUDE_DIR}")
MESSAGE("** FOUND CHAKRACORE:  ${CHAKRACORE_LIBRARY}")

set(CHAKRACORE_INCLUDE_DIRS ${CHAKRACORE_INCLUDE_DIR})
set(CHAKRACORE_LIBRARIES ${CHAKRACORE_LIBRARY})

set(CHAKRACORE_VERSION_STRING "1.4.1")

mark_as_advanced(CHAKRACORE_LIBRARY CHAKRACORE_LIBRARIES CHAKRACORE_INCLUDE_DIR CHAKRACORE_INCLUDE_DIRS CHAKRACORE_VERSION_STRING)

