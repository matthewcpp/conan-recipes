cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Threads REQUIRED)

set(common_src include/ezmidi/ezmidi.h src/common.cpp)

if (WIN32)
    set(platform_libs Winmm.lib)
elseif(APPLE)
    set(platform_libs "-framework CoreMIDI" "-framework CoreFoundation")
else()
    set(platform_libs "-lasound")
endif()

add_executable(test_package test_package.cpp)
target_link_libraries(test_package ${CONAN_LIBS} ${platform_libs} Threads::Threads)
set_target_properties(test_package PROPERTIES CXX_STANDARD 11 CXX_STANDARD_REQUIRED ON)
