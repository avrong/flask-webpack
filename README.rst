Flask-Webpack-Current
^^^^^^^^^^^^^^^^^^^^^
|Build status|

**Flask-Webpack for latest webpack-manifest-plugin**.


Installation
^^^^^^^^^^^^

``pip install git+https://github.com/avrong/flask-webpack-current``


Quick start
^^^^^^^^^^^

::

    from flask import Flask
    from flask_webpack_current import Webpack

    webpack = Webpack()

    app = Flask(__name__)
    webpack.init_app(app)


Settings
^^^^^^^^

``Flask-Webpack`` is configured like most Flask extensions. Here's the available
options:

- ``WEBPACK_MANIFEST_PATH``: default ``None``
    - **Required:** You may consider using ``./build/manifest.json``, it's up to you.

- ``WEBPACK_ASSETS_URL``: default ``None``
    - **Required:** You would set this to your full domain name or CDN.


Global template tags
^^^^^^^^^^^^^^^^^^^^

- **asset_url_for(asset_relative_path)** to resolve an asset name
- **javascript_tag(\*asset_relative_paths)** to write out 1 or more script tags
- **stylesheet_tag(\*asset_relative_paths)** to write out 1 or more stylesheet tags

Both the javascript and stylesheet tags accept multiple arguments. If you give
it more than argument it will create as many tags as needed.


About
^^^^^

Managing assets can be a serious burden. Here's just a few things you get by
using this package:

- Minify assets
- Attach vendor prefixes to your CSS automatically
- Optimize image sizes
- Leverage the CommonJS module system to organize your Javascript
- Compile Markdown
- Compile 20+ client side template languages
- Compile LESS, SASS and any other CSS pre-processor you can imagine
- Compile Typescript, Coffeescript and any other *to-javascript* language
- Compile Ecmascript 6 (ES) down to ES 5
- Compile React JSX to JS with hot module reloading
- Near instant compile times, ~20-50ms is common on my workstation
- Optionally get source maps in development mode
- Serve your assets from a tricked out local development asset server
- Cache all assets forever because their file names get md5-tagged
- The only runtime you need other than Python is NodeJS
- Never deal with file watchers again because it's all taken care of for you
- And much more...

All of the features above are the direct result of using `Webpack <http://webpack.github.io/>`_
to manage your assets. The huge win here besides the obvious is that the
functionality is outside of this package.

That means you have free reign to pick and choose what you want without
having to worry about Flask-Webpack versions. If a new Webpack plugin becomes
available, you can use it immediately.


How does it work?
-----------------

It expects you to have built a manifest file and it handles the rest. You can
build this manifest file using ``webpack-manifest-plugin`` plugin.

This process is done automatically upon starting the dev asset server or building
your assets to prepare for a production release. All of that is taken care of in
the ``webpack.config.js`` file.


What does this package do then?
-------------------------------

It sets up a few template tags so you can access the assets inside of your
jinja templates.

**It means you can type this:**

``<img src="{{ asset_url_for('images/hamburger.svg') }}" alt="Hamburger">``

**...and once your jinja template has been compiled, you will see this:**

``<img src="images/hamburger.d2cb0dda3e8313b990e8dcf5e25d2d0f.svg" alt="Hamburger">``

Now you can happily tell your frontend proxy to cache that hamburger image for
an entire year. If you ever change the hamburger, the md5 will change but you
do not need to change any of your templates because the ``asset_url_for``
tag knows how to look it up.


Help! My assets do not work outside of development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I see, so basically the problem is you're using the ``url()`` function in your
stylesheets and are referencing a relative path to an asset, such as:

``src: url('../../fonts/CoolFont.eot')``

The above works in development mode because that's where the file is 
located but in production mode the asset is not there. The ``asset_url_for`` 
template helper handles all of this for you on the server side but now you need
some assistance  on the client side as well.

You have a few options here depending on if you're using CSS, SASS or something
else. If you're using straight CSS you will need to pre-prend all of your paths
with a special identifier.

If you were to re-write the example from above, it would now be:

``src: url('~!file!../../fonts/CoolFont.eot')``

That will automatically get expanded to a path that works in every environment.

If you're using SASS you can create your own function to make things easier to
work with on a day to day basis. Something like this should suffice:

::

    @function asset-url($path) {
      @return url('~!file!' + $path);
    }

Now you can call it like this and everything will work:

``src: asset-url('../../fonts/CoolFont.eot')``

Feel free to make additional helper functions that let you abstract away the
relative prefix such as ``font-url`` or ``image-url``. It really depends on how
your assets are set up.

Contributors
^^^^^^^^^^^^

- Nick Janetakis <nick.janetakis@gmail.com>
- Alexey Trifonov <avrong@outlook.com>

.. |Build status| image:: https://secure.travis-ci.org/avrong/flask-webpack-current.png
   :target: https://travis-ci.org/avrong/flask-webpack-current
