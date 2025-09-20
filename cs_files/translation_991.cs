public SinglePositionTokenStream(string word){
    wordBytes = Encoding.GetBytes(word);
    position = -1;
}