public FileBasedConfig(NGit.Config base, FilePath cfgLocation, FS fs){
    base.Config = base;
    this.configFile = cfgLocation;
    this.fs = fs;
}