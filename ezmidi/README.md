# ezmidi

Conan file for building package of the [ezmidi](https://github.com/matthewcpp/ezmidi) library from github.

## Configure conan

Add The `matthewcpp` remote
```
conan remote add matthewcpp https://api.bintray.com/conan/matthewcpp/conan 
```

### Buildig the package

Update the version string in `conanfile.py` with the short commit hash for the version to bump to.
Update the `git_revision` field with the full commit hash of the version.

### Pushing the package
```
conan create . matthewcpp/master
conan upload ezmidi/565114c@matthewcpp/master -r=matthewcpp
```
Note: Use API key for the password
