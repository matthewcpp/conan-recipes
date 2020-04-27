# conan-vma

Conan file for building package of the [Vulkan Memory Allocator](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator) library from github.

### Buildig the package

Update the version string in `conanfile.py` with the short commit hash for the version to bump to.
Update the `git_revision` field with the full commit hash of the version.


### Pushing the package
```
conan create . matthewcpp/master
conan upload VulkanMemoryAllocator/25d9b2c@matthewcpp/master -r=matthewcpp
```
Note: Use API key for the password
