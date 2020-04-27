from conans import ConanFile, CMake, tools


class VulkanmemoryallocatorConan(ConanFile):
    name = "VulkanMemoryAllocator"
    version = "25d9b2c"
    license = "MIT"
    url = "https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator"
    description = "Easy to integrate Vulkan memory allocation library"
    topics = ("vulkan")
    no_copy_source = True
    build_policy = "always"
    git_revision = "25d9b2c0ec41853f4a2c9ae432cc12dadbc94836"

    def source(self):
        tools.download("https://raw.githubusercontent.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/{}/src/vk_mem_alloc.h".format(self.git_revision), "vk_mem_alloc.h")

    def package(self):
        self.copy("vk_mem_alloc.h", dst="include")

    def package_id(self):
        self.info.header_only()


