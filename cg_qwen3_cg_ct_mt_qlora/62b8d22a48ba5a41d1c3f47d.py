public Object pop(Object key, Object defaultValue) {
        Object result = get(key);
        if (result == null && defaultValue != null)
            return defaultValue;
        else if (result == null)
            throw new NoSuchElementException();
        else
            remove(key);
        return result;
    }