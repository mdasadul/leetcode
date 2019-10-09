import string
class Codec:
    urltocode ={}
    codetourl ={}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        while longUrl not in self.urltocode:
            code = ''
            for _ in range(6):
                code +=random.choice(string.letters+string.digits)
            if code not in self.codetourl:
                self.urltocode[longUrl] = code
                self.codetourl[code] =longUrl
        return 'http://tinyurl.com/'+self.urltocode[longUrl]
        
            
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        return self.codetourl[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))