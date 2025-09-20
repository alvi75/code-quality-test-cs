public virtual InputStream OpenResource(string resource resource){
    Stream stream = null;
    try{
        if (clazz != null){
            stream = clazz.GetResource(resource);
        }
        else{
            stream = loader.GetResource(resource);
            if (stream == null){
                throw new IOException("Resource not found: " + resource);
            }
        }
    }
    return stream;
}