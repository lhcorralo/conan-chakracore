project(ChakraCoreTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

#set(CARES_USE_STATIC TRUE)
find_package (ChakraCore REQUIRED)
include_directories(${CHAKRACORE_INCLUDE_DIR})
add_definitions(${ChakraCore_DEFINITIONS})
add_executable(HelloWorld HelloWorld.cpp)
target_link_libraries(HelloWorld ${CHAKRACORE_LIBRARY})
