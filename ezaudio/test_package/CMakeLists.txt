cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(common_src include/ezaudio/ezaudio.h src/common.cpp)

if (WIN32)
    set(platform_libs setupapi.lib winmm.lib imm32.lib version.lib)
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(platform_libs "-framework AudioToolbox")
endif()

add_executable(test_package test_package.cpp)
target_link_libraries(test_package ${CONAN_LIBS} ${platform_libs})
set_target_properties(test_package PROPERTIES CXX_STANDARD 11 CXX_STANDARD_REQUIRED ON)

# enable_testing()
# add_test(NAME test_package
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND test_package)
