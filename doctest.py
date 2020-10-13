    """
    >>> cache = Cache()
    >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
    >>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
    >>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")

    >>> content4 = ContentItem(1004, 50, "Content-Type: 1", "110010")
    >>> content5 = ContentItem(1001, 51, "Content-Type: 1", "110011")
    >>> content6 = ContentItem(1007, 155, "Content-Type: 1", "10011011")

    >>> content7 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
    >>> content8 = ContentItem(1002, 14, "Content-Type: 2", "<html><h2>'PSU'</h2></html>")
    >>> content9 = ContentItem(1006, 170, "Content-Type: 2", "<html><button>'Click Me'</button></html>")

    >>> cache.insert(content1, 'lru')
    'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
    >>> cache.insert(content2, 'lru')
    'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
    >>> cache.insert(content3, 'lru')
    'Insertion not allowed. Content size is too large.'

    >>> cache.insert(content4, 'lru')
    'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
    >>> cache.insert(content5, 'lru')
    'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
    >>> cache.insert(content6, 'lru')
    'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'

    >>> cache.insert(content7, 'lru')
    "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
    >>> cache.insert(content8, 'lru')
    "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
    >>> cache.insert(content9, 'lru')
    "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
    >>> cache
    L1 CACHE:
    REMAINING SPACE:177
    ITEMS:2
    LIST:
    [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
    [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
    <BLANKLINE>
    <BLANKLINE>
    L2 CACHE:
    REMAINING SPACE:45
    ITEMS:1
    LIST:
    [CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011]
    <BLANKLINE>
    <BLANKLINE>
    L3 CACHE:
    REMAINING SPACE:16
    ITEMS:2
    LIST:
    [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
    [CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>]
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.hierarchy[0].clear()
    'Cleared cache!'
    >>> cache.hierarchy[1].clear()
    'Cleared cache!'
    >>> cache.hierarchy[2].clear()
    'Cleared cache!'
    >>> cache
    L1 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    L2 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    L3 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.insert(content1, 'mru')
    'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
    >>> cache.insert(content2, 'mru')
    'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
    >>> cache.retrieveContent(content1)
    CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA
    >>> cache.retrieveContent(content2)
    CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD
    >>> cache.retrieveContent(content3)
    'Cache miss!'

    >>> cache.insert(content5, 'lru')
    'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
    >>> cache.insert(content6, 'lru')
    'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'
    >>> cache.insert(content4, 'lru')
    'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'


    >>> cache.insert(content7, 'mru')
    "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
    >>> cache.insert(content8, 'mru')
    "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
    >>> cache.insert(content9, 'mru')
    "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
    >>> cache
    L1 CACHE:
    REMAINING SPACE:177
    ITEMS:2
    LIST:
    [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
    [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
    <BLANKLINE>
    <BLANKLINE>
    L2 CACHE:
    REMAINING SPACE:150
    ITEMS:1
    LIST:
    [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
    <BLANKLINE>
    <BLANKLINE>
    L3 CACHE:
    REMAINING SPACE:12
    ITEMS:2
    LIST:
    [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
    [CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>]
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>

    >>> cache.clear()
    'Cache cleared!'
    >>> contentA = ContentItem(2000, 52, "Content-Type: 2", "GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1")
    >>> contentB = ContentItem(2001, 76, "Content-Type: 2", "GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1")
    >>> contentC = ContentItem(2002, 11, "Content-Type: 2", "GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1")
    >>> cache.insert(contentA, 'lru')
    'INSERTED: CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1'
    >>> cache.insert(contentB, 'lru')
    'INSERTED: CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1'
    >>> cache.insert(contentC, 'lru')
    'INSERTED: CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1'
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.retrieveContent(contentC)
    CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.retrieveContent(contentA)
    CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.retrieveContent(contentC)
    CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    >>> contentD = ContentItem(2002, 11, "Content-Type: 2", "GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1")
    >>> cache.insert(contentD, 'lru')
    'Insertion of content item 2002 not allowed. Content already in cache.'
    >>> contentE = ContentItem(2000, 52, "Content-Type: 2", "GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1")
    >>> cache.updateContent(contentE)
    'UPDATED: CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1'
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1]
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    
    """
