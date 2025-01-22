def get(): return """<!DOCTYPE html>
<html>
<head>
    <title>posts</title>
    <style>
    body {
        background-color: #89c0e0; 
    }
    .heading{
        color: Blue;
    }

    .postbox{
        border: 2px double black;
        background: #bbe7f0;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
        width: 40vw;
        height: 40vh;
        overflow: auto;
        z-index: 10;
        }

        .pic{
            border: 2px double blue;
            width: 64px;
            height: 64px;
            margin: 0px 10px;
        }

        hr {
            height: 3px;
            background-color: black;
            border: none;
            margin: 0;
            padding: 0;
        }

        .odd{
            background: #6999b5;
            margin: 0;
            padding: 0;
            z-index: 3;
        }
        
        .even{
            background: #ede8cc;
            margin: none;
            z-index: 3;
        }

    </style>
</head>
<body>
    <h1 class="heading" align="center">Posts</h1>

    <div class="postbox">
        <div class="odd">
            <img src="/html/logo.png" class="pic">
            <span>&emsp; Hello!<span>
            <span>&emsp;&emsp; 3 days ago &emsp;&emsp; 10 views </span>
            <hr>
        </div>

        <div class="even">
            <img src="/html/cat.jpg" class="pic">
            <span>&emsp; Yo<span>
            <span>&emsp;&emsp; 10 days ago &emsp;&emsp; 32 views </span>
            <hr>
        </div>

        <div class="odd">
            <img src="/html/3.jpg" class="pic">
            <span>&emsp; What's up<span>
            <span>&emsp;&emsp; 6 days ago &emsp;&emsp; 52 views </span>
            <hr>
        </div>

        <div class="even">
            <img src="/html/alfred-marko.png" class="pic">
            <span>&emsp; Hey<span>
            <span>&emsp;&emsp; 4 days ago &emsp;&emsp; 44 views </span>
            <hr>
        </div>

        <div class="odd">
            <img src="/html/kermit.jpg" class="pic">
            <span>&emsp; What's going on?<span>
            <span>&emsp;&emsp; 12 days ago &emsp;&emsp; 27 views </span>
            <hr>
        </div>

        <div class="even">
            <img src="/html/peppa.jpg" class="pic">
            <span>&emsp; Howdy<span>
            <span>&emsp;&emsp; 5 days ago &emsp;&emsp; 13 views </span>
            <hr>
        </div>

        <div class="odd">
            <img src="/html/shrek.jpg" class="pic">
            <span>&emsp; Good morning!<span>
            <span>&emsp;&emsp; 1 days ago &emsp;&emsp; 36 views </span>
            <hr>
        </div>

        <div class="even">
            <img src="/html/sponge.jpg" class="pic">
            <span>&emsp; Bonjour!<span>
            <span>&emsp;&emsp; 15 days ago &emsp;&emsp; 23 views </span>
            <hr>
        </div>

        <div class="odd">
            <img src="/html/mouse.jpg" class="pic">
            <span>&emsp; hi<span>
            <span>&emsp;&emsp; 11 days ago &emsp;&emsp; 50 views </span>
            <hr>
        </div>

        <div class="even">
            <img src="/html/kirby.png" class="pic">
            <span>&emsp; Aloha<span>
            <span>&emsp;&emsp; 2 days ago &emsp;&emsp; 20 views </span>
            <hr>
        </div>

    </div>
</body>
</html>"""