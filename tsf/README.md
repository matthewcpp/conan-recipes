# conan-tsf

Conan file for building package of the [TinySoundFont](https://github.com/schellingb/TinySoundFont) library from github.

### Buildig the package

Update the version string in `conanfile.py` with the short commit hash for the version to bump to.
Update the `git_revision` field with the full commit hash of the version.

### Pushing the package
```
conan create . matthewcpp/master
conan upload TinySoundFont/21c07c0@matthewcpp/master -r=matthewcpp
```
Note: Use API key for the password
