from pynput import keyboard, mouse
import time

games_raw = """
<!DOCTYPE html>
<html lang="en-US">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>50+ Best Online Games to Play With Friends | Man of Many</title><link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&#038;display=swap" /><style id="" media="print" onload="this.media='all'">/* cyrillic-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2JL7SUc.woff2) format('woff2');
  unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
}
/* cyrillic */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa0ZL7SUc.woff2) format('woff2');
  unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
}
/* greek-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2ZL7SUc.woff2) format('woff2');
  unicode-range: U+1F00-1FFF;
}
/* greek */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1pL7SUc.woff2) format('woff2');
  unicode-range: U+0370-03FF;
}
/* vietnamese */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2pL7SUc.woff2) format('woff2');
  unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;
}
/* latin-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa25L7SUc.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* cyrillic-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2JL7SUc.woff2) format('woff2');
  unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
}
/* cyrillic */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa0ZL7SUc.woff2) format('woff2');
  unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
}
/* greek-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2ZL7SUc.woff2) format('woff2');
  unicode-range: U+1F00-1FFF;
}
/* greek */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1pL7SUc.woff2) format('woff2');
  unicode-range: U+0370-03FF;
}
/* vietnamese */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2pL7SUc.woff2) format('woff2');
  unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;
}
/* latin-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa25L7SUc.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* cyrillic-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2JL7SUc.woff2) format('woff2');
  unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
}
/* cyrillic */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa0ZL7SUc.woff2) format('woff2');
  unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
}
/* greek-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2ZL7SUc.woff2) format('woff2');
  unicode-range: U+1F00-1FFF;
}
/* greek */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1pL7SUc.woff2) format('woff2');
  unicode-range: U+0370-03FF;
}
/* vietnamese */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa2pL7SUc.woff2) format('woff2');
  unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;
}
/* latin-ext */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa25L7SUc.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(/fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
</style><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&#038;display=swap" /></noscript>
<link rel="profile" href="https://gmpg.org/xfn/11">
<link rel="pingback" href="https://manofmany.com/xmlrpc.php">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=2">
<meta name="format-detection" content="telephone=no">
<meta name="google-site-verification" content="FGn9k48DZ9UTUzNSU6m91J7hj4d80P5mcdWTN-URp4U" />
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="cf-2fa-verify" content="110b51e9c86506f">
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
<script>
      (function() {
        window.dm = window.dm || {AjaxData: []};
        window.dm.AjaxEvent = function(et, d, ssid, ad) {
          dm.AjaxData.push({et: et, d: d, ssid: ssid, ad: ad});
          if (typeof window.DotMetricsObj != 'undefined') {DotMetricsObj.onAjaxDataUpdate();}
        };
        var d = document, h = d.getElementsByTagName('head')[0], s = d.createElement('script');
        s.type = 'text/javascript';
        s.async = true;
        s.src = 'https://au-script.dotmetrics.net/door.js?d=' + document.location.host + '&t=gaming';
        h.appendChild(s);
      }());
    </script>

<script>
    </script>


<meta name="description" content="You&#039;ll never have to play online multiplayer games solo again with this extensive guide to the best online games to play with friends." />
<link rel="canonical" href="https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="article" />
<meta property="og:title" content="50+ Best Online Games to Play With Friends | Man of Many" />
<meta property="og:description" content="You&#039;ll never have to play online multiplayer games solo again with this extensive guide to the best online games to play with friends." />
<meta property="og:url" content="https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends" />
<meta property="og:site_name" content="Man of Many" />
<meta property="article:publisher" content="https://www.facebook.com/manofmany" />
<meta property="article:published_time" content="2021-07-25T23:00:26+00:00" />
<meta property="article:modified_time" content="2023-04-15T04:07:34+00:00" />
<meta property="og:image" content="https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="900" />
<meta property="og:image:type" content="image/jpeg" />
<meta name="author" content="Michael Vane" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:creator" content="@manofmany" />
<meta name="twitter:site" content="@manofmany" />

<link rel='dns-prefetch' href='//vzqmjzid.manofmany.com' />
<link rel='dns-prefetch' href='//maps.googleapis.com' />
<link rel='dns-prefetch' href='//maps.gstatic.com' />
<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel='dns-prefetch' href='//fonts.gstatic.com' />
<link rel='dns-prefetch' href='//use.fontawesome.com' />
<link rel='dns-prefetch' href='//ajax.googleapis.com' />
<link rel='dns-prefetch' href='//apis.google.com' />
<link rel='dns-prefetch' href='//google-analytics.com' />
<link rel='dns-prefetch' href='//www.google-analytics.com' />
<link rel='dns-prefetch' href='//ssl.google-analytics.com' />
<link rel='dns-prefetch' href='//www.googletagmanager.com' />
<link rel='dns-prefetch' href='//www.googletagservices.com' />
<link rel='dns-prefetch' href='//googleads.g.doubleclick.net' />
<link rel='dns-prefetch' href='//adservice.google.com' />
<link rel='dns-prefetch' href='//pagead2.googlesyndication.com' />
<link rel='dns-prefetch' href='//tpc.googlesyndication.com' />
<link rel='dns-prefetch' href='//youtube.com' />
<link rel='dns-prefetch' href='//i.ytimg.com' />
<link rel='dns-prefetch' href='//player.vimeo.com' />
<link rel='dns-prefetch' href='//api.pinterest.com' />
<link rel='dns-prefetch' href='//assets.pinterest.com' />
<link rel='dns-prefetch' href='//connect.facebook.net' />
<link rel='dns-prefetch' href='//platform.twitter.com' />
<link rel='dns-prefetch' href='//syndication.twitter.com' />
<link rel='dns-prefetch' href='//platform.instagram.com' />
<link rel='dns-prefetch' href='//referrer.disqus.com' />
<link rel='dns-prefetch' href='//c.disquscdn.com' />
<link rel='dns-prefetch' href='//cdnjs.cloudflare.com' />
<link rel='dns-prefetch' href='//pixel.wp.com' />
<link rel='dns-prefetch' href='//disqus.com' />
<link rel='dns-prefetch' href='//s.gravatar.com' />
<link rel='dns-prefetch' href='//0.gravatar.com' />
<link rel='dns-prefetch' href='//2.gravatar.com' />
<link rel='dns-prefetch' href='//1.gravatar.com' />
<link rel='dns-prefetch' href='//sitename.disqus.com' />
<link rel='dns-prefetch' href='//s7.addthis.com' />
<link rel='dns-prefetch' href='//platform.linkedin.com' />
<link rel='dns-prefetch' href='//w.sharethis.com' />
<link rel='dns-prefetch' href='//s0.wp.com' />
<link rel='dns-prefetch' href='//s1.wp.com' />
<link rel='dns-prefetch' href='//s2.wp.com' />
<link rel='dns-prefetch' href='//stats.wp.com' />
<link rel='dns-prefetch' href='//ajax.microsoft.com' />
<link rel='dns-prefetch' href='//ajax.aspnetcdn.com' />
<link rel='dns-prefetch' href='//s3.amazonaws.com' />
<link rel='dns-prefetch' href='//code.jquery.com' />
<link rel='dns-prefetch' href='//stackpath.bootstrapcdn.com' />
<link rel='dns-prefetch' href='//github.githubassets.com' />
<link rel='dns-prefetch' href='//ad.doubleclick.net' />
<link rel='dns-prefetch' href='//stats.g.doubleclick.net' />
<link rel='dns-prefetch' href='//cm.g.doubleclick.net' />
<link rel='dns-prefetch' href='//stats.buysellads.com' />
<link rel='dns-prefetch' href='//s3.buysellads.com' />
<link rel='dns-prefetch' href='//ssc-cms.33across.com' />
<link rel='dns-prefetch' href='//de.tynt.com' />
<link rel='dns-prefetch' href='//biddr.brealtime.com' />
<link rel='dns-prefetch' href='//cdn-gl.imrworldwide.com' />
<link rel='dns-prefetch' href='//sync.1rx.io' />
<link rel='dns-prefetch' href='//sync.targeting.unrulymedia.com' />
<link rel='dns-prefetch' href='//sync.mathtag.com' />
<link href='https://fonts.gstatic.com' crossorigin rel='preconnect' />
<link rel="alternate" type="application/rss+xml" title="Man of Many &raquo; Feed" href="https://manofmany.com/feed" />
<style id='acf-mom-newsletter-style-inline-css' type='text/css'>


/*# sourceMappingURL=/wp-content/themes/manofmany/dist/sourcemaps/../newsletter.min.css.map*/
</style>
<style id='acf-mom-jwplayer-style-inline-css' type='text/css'>


/*# sourceMappingURL=/wp-content/themes/manofmany/dist/sourcemaps/../jwplayer.min.css.map*/
</style>
<style id='safe-svg-svg-icon-style-inline-css' type='text/css'>
.safe-svg-cover .safe-svg-inside{display:inline-block;max-width:100%}.safe-svg-cover svg{height:100%;max-height:100%;max-width:100%;width:100%}

</style>
<style id='classic-theme-styles-inline-css' type='text/css'>
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
</style>
<style id='global-styles-inline-css' type='text/css'>
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
.wp-block-pullquote{font-size: 1.5em;line-height: 1.6;}
</style>
<link data-minify="1" rel='stylesheet' id='cookie-law-info-css' href='https://manofmany.com/wp-content/cache/min/1/wp-content/plugins/webtoffee-gdpr-cookie-consent/public/css/cookie-law-info-public.css?ver=1691850918' type='text/css' media='all' />
<link data-minify="1" rel='stylesheet' id='cookie-law-info-gdpr-css' href='https://manofmany.com/wp-content/cache/min/1/wp-content/plugins/webtoffee-gdpr-cookie-consent/public/css/cookie-law-info-gdpr.css?ver=1691850918' type='text/css' media='all' />
<style id='cookie-law-info-gdpr-inline-css' type='text/css'>
.cli-modal-content, .cli-tab-content { background-color: #ffffff; }.cli-privacy-content-text, .cli-modal .cli-modal-dialog, .cli-tab-container p, a.cli-privacy-readmore { color: #000000; }.cli-tab-header { background-color: #f2f2f2; }.cli-tab-header, .cli-tab-header a.cli-nav-link,span.cli-necessary-caption,.cli-switch .cli-slider:after { color: #000000; }.cli-switch .cli-slider:before { background-color: #ffffff; }.cli-switch input:checked + .cli-slider:before { background-color: #ffffff; }.cli-switch .cli-slider { background-color: #e3e1e8; }.cli-switch input:checked + .cli-slider { background-color: #28a745; }.cli-modal-close svg { fill: #000000; }.cli-tab-footer .wt-cli-privacy-accept-all-btn { background-color: #00acad; color: #ffffff}.cli-tab-footer .wt-cli-privacy-accept-btn { background-color: #00acad; color: #ffffff}.cli-tab-header a:before{ border-right: 1px solid #000000; border-bottom: 1px solid #000000; }
</style>
<link rel='stylesheet' id='mom-theme-style-css' href='https://manofmany.com/wp-content/themes/manofmany/dist/main.min.css?ver=9cb0b7db0fce2469e763a32238a9f3f6' type='text/css' media='all' />
<link rel='stylesheet' id='mom-post-style-css' href='https://manofmany.com/wp-content/themes/manofmany/dist/post.min.css?ver=9cb0b7db0fce2469e763a32238a9f3f6' type='text/css' media='all' />
<style id='rocket-lazyload-inline-css' type='text/css'>
.rll-youtube-player{position:relative;padding-bottom:56.23%;height:0;overflow:hidden;max-width:100%;}.rll-youtube-player:focus-within{outline: 2px solid currentColor;outline-offset: 5px;}.rll-youtube-player iframe{position:absolute;top:0;left:0;width:100%;height:100%;z-index:100;background:0 0}.rll-youtube-player img{bottom:0;display:block;left:0;margin:auto;max-width:100%;width:100%;position:absolute;right:0;top:0;border:none;height:auto;-webkit-transition:.4s all;-moz-transition:.4s all;transition:.4s all}.rll-youtube-player img:hover{-webkit-filter:brightness(75%)}.rll-youtube-player .play{height:100%;width:100%;left:0;top:0;position:absolute;background:url(https://manofmany.com/wp-content/plugins/wp-rocket/assets/img/youtube.png) no-repeat center;background-color: transparent !important;cursor:pointer;border:none;}
</style>
<script type='text/javascript' src='https://manofmany.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.0' id='jquery-core-js'></script>
<script type='text/javascript' src='https://manofmany.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1' id='jquery-migrate-js' defer></script>
<script type='text/javascript' id='cookie-law-info-js-extra'>
/* <![CDATA[ */
var Cli_Data = {"nn_cookie_ids":["__sharethis_cookie_test__","__cf_bm","CONSENT","_gat_UA-34930460-1","_gid","_ga","IDE","VISITOR_INFO1_LIVE","YSC","fr","_fbp","test_cookie","XSRF-TOKEN","_app_session","_gfpc","owner_token","_lr_geo_location","akacd_manofmany"],"non_necessary_cookies":{"necessary":["cookielawinfo-checkbox-advertisement","XSRF-TOKEN"],"functional":["__sharethis_cookie_test__","__cf_bm"],"analytics":["CONSENT","_gat_UA-34930460-1","_ga","_gid"],"advertisement":["__gads","VISITOR_INFO1_LIVE","IDE","fr","YSC","test_cookie","_fbp"],"others":["_gfpc","_app_session","owner_token","_lr_geo_location","akacd_manofmany"]},"cookielist":{"necessary":{"id":112908,"status":true,"priority":0,"title":"Necessary","strict":true,"default_state":false,"ccpa_optout":false,"loadonstart":false},"functional":{"id":112909,"status":true,"priority":5,"title":"Functional","strict":false,"default_state":true,"ccpa_optout":false,"loadonstart":false},"performance":{"id":112910,"status":true,"priority":4,"title":"Performance","strict":false,"default_state":true,"ccpa_optout":false,"loadonstart":false},"analytics":{"id":112911,"status":true,"priority":3,"title":"Analytics","strict":false,"default_state":true,"ccpa_optout":false,"loadonstart":false},"advertisement":{"id":112912,"status":true,"priority":2,"title":"Advertisement","strict":false,"default_state":true,"ccpa_optout":false,"loadonstart":false},"others":{"id":112913,"status":true,"priority":1,"title":"Others","strict":false,"default_state":true,"ccpa_optout":false,"loadonstart":false}},"ajax_url":"https:\/\/manofmany.com\/wp-admin\/admin-ajax.php","current_lang":"en","security":"515c3baf55","eu_countries":["GB"],"geoIP":"enabled","use_custom_geolocation_api":"","custom_geolocation_api":"https:\/\/geoip.cookieyes.com\/geoip\/checker\/result.php","consentVersion":"1","strictlyEnabled":["necessary","obligatoire"],"cookieDomain":"","privacy_length":"250","ccpaEnabled":"1","ccpaRegionBased":"1","ccpaBarEnabled":"1","ccpaType":"ccpa_gdpr","triggerDomRefresh":"","secure_cookies":""};
var log_object = {"ajax_url":"https:\/\/manofmany.com\/wp-admin\/admin-ajax.php"};
/* ]]> */
</script>
<script type='text/javascript' src='https://manofmany.com/wp-content/plugins/webtoffee-gdpr-cookie-consent/public/js/cookie-law-info-public.js?ver=2.3.9' id='cookie-law-info-js' defer></script>
<script type='text/javascript' id='cookie-law-info-ccpa-js-extra'>
/* <![CDATA[ */
var ccpa_data = {"opt_out_prompt":"Do you really wish to opt out?","opt_out_confirm":"Confirm","opt_out_cancel":"Cancel"};
/* ]]> */
</script>
<script type='text/javascript' src='https://manofmany.com/wp-content/plugins/webtoffee-gdpr-cookie-consent/admin/modules/ccpa/assets/js/cookie-law-info-ccpa.js?ver=2.3.9' id='cookie-law-info-ccpa-js' defer></script>
<link rel="alternate" type="application/json+oembed" href="https://manofmany.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fmanofmany.com%2Fentertainment%2Fgaming%2Fbest-online-games-to-play-with-friends" />
<link rel="alternate" type="text/xml+oembed" href="https://manofmany.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fmanofmany.com%2Fentertainment%2Fgaming%2Fbest-online-games-to-play-with-friends&#038;format=xml" />
<link rel="apple-touch-icon" sizes="57x57" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/apple-icon-180x180.png">
<link rel="icon" type="image/png" sizes="192x192" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/android-icon-192x192.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="96x96" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="16x16" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/favicon-16x16.png">
<link rel="manifest" href="https://manofmany.com/wp-content/themes/manofmany/images/favicon/manifest.json">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="msapplication-TileImage" content="https://manofmany.com/wp-content/themes/manofmany/images/favicon/ms-icon-144x144.png">
<meta name="msapplication-tap-highlight" content="no">
<meta name="theme-color" content="#000000">
<script type="rocketlazyloadscript" defer data-rocket-src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js" data-rocket-type="text/javascript"></script>

<script>
    
    const PWT = {}; //Initialize Namespace
    let gptRan = false;

    PWT.jsLoaded = function() { //PubMatic pwt.js on load callback is used to load GPT
      loadGPT();
    };

    const loadGPT = function() {
      // Check the gptRan flag
      if (!gptRan) {
        gptRan = true;
        const gads = document.createElement('script');
        const useSSL = 'https:' === document.location.protocol;
        gads.src = (useSSL ? 'https:' : 'http:') + '//securepubads.g.doubleclick.net/tag/js/gpt.js';
        const node = document.getElementsByTagName('script')[0];
        node.parentNode.insertBefore(gads, node);
      }
    };

    // Failsafe to call gpt. 500 ms timeout can be updated as per publisher preference.
    setTimeout(loadGPT, 500);

    (function() {
      const purl = window.location.href;
      const url = '//ads.pubmatic.com/AdServer/js/pwt/163463/10608';
      let profileVersionId = '';
      if (purl.indexOf('pwtv=') > 0) {
        const regexp = /pwtv=(.*?)(&|$)/g;
        const matches = regexp.exec(purl);
        if (matches.length >= 2 && matches[1].length > 0) {
          profileVersionId = '/' + matches[1];
        }
      }
      const wtads = document.createElement('script');
      wtads.async = true;
      wtads.type = 'text/javascript';
      wtads.src = url + profileVersionId + '/pwt.js';
      const node = document.getElementsByTagName('script')[0];
      node.parentNode.insertBefore(wtads, node);
    })();
  </script>
<script>
    window.googletag = window.googletag || {cmd: []};

        window.gamVars = {
      'site': 'ManOfMany',
      'kv': {"pagetype":"article","cat":["entertainment"],"subcat":["gaming"],"tags":["fortnite","halo","nintendo","nintendo-switch","pc","playstation","xbox"],"pageID":"377048","title":"best-online-games-to-play-with-friends","env":"production"}    };

        // Prepare GAM targeting variables
    const gamData = {
      'kv': window.gamVars.kv,
      'sizeMap': {"headerdesk":[[[992,0],[970,250]],[[768,0],[728,90]],[[0,0],[]]],"footerdesk":[[[768,0],[728,90]],[[0,0],[]]],"anchor":[[[768,0],[]],[[0,0],[[320,50],[300,50]]]],"midpage":[[[992,0],[[970,250],[970,90],[728,90]]],[[768,0],[728,90]],[[0,0],[[336,280],[300,300],[300,250],[320,100],[320,50],[300,50]]]],"midpagemob":[[[768,0],[]],[[0,0],[[336,280],[300,300],[300,250],[320,100],[320,50],[300,50]]]],"sidebarmrec":[[[992,0],[300,250]],[[0,0],[]]],"sidebarhalf":[[[992,0],[[300,600],[160,600]]],[[0,0],[]]],"incontent":[[[1199,0],[[728,90],[640,360],["fluid"]]],[[992,0],[[336,280],[300,300],[300,250],[320,100],[576,324],["fluid"]]],[[0,0],[[336,280],[300,300],[300,250],[320,100],[320,180],["fluid"]]]]}    };

    // Ad Tester (add "?adtest=testvalue" to url, inserts KV for targeting). Can also capture other URL query strings.
    const kvAdTest = '';

    // Check browser width for skins
    const viewportWidth = document.documentElement.clientWidth;
    const showSkin = viewportWidth >= 1440 ? 'Y' : 'N';

        googletag.cmd.push(function() {
      googletag.pubads().setTargeting('adtest', [kvAdTest]);
      googletag.pubads().setTargeting('skin', [showSkin]);

      if (gamData.kv) {
        Object.keys(gamData.kv).forEach(function(key) {
          googletag.pubads().setTargeting(key, gamData.kv[key]);
        });
      }

      googletag.pubads().setCentering(true);
      googletag.pubads().collapseEmptyDivs();

      // Enable lazy-loading for all ad slots (at page level)
      googletag.pubads().enableLazyLoad({fetchMarginPercent: 200, renderMarginPercent: 50, mobileScaling: 2.0});

      // In-view refresh settings
      const adRefreshKey = 'refresh';
      const adRefreshFlag = 'true';
      const adRefreshTime = 60;
      googletag.pubads().addEventListener('impressionViewable', function(event) {
        const slot = event.slot;
        if (slot.getTargeting(adRefreshKey).indexOf(adRefreshFlag) > -1) {
          setTimeout(function() {
            googletag.pubads().refresh([slot]);
          }, adRefreshTime * 1000);
        }
      });

      
      // Enable services
      googletag.setAdIframeTitle('Advertisement');
      googletag.enableServices();

      // Refresh ads on screen size changes
      if (window.addEventListener) {
        window.addEventListener('resize', browserResize);
      } else if (window.attachEvent) {
        window.attachEvent('onresize', browserResize);
      }

      let InitialResize = window.innerWidth;

      function browserResize() {
        const afterResize = window.innerWidth;
        if (
          (InitialResize < 1200 && afterResize >= 1200) || (InitialResize >= 1200 && afterResize < 1200) ||
          (InitialResize < 992 && afterResize >= 992) || (InitialResize >= 992 && afterResize < 992) ||
          (InitialResize < 768 && afterResize >= 768) || (InitialResize >= 768 && afterResize < 768) ||
          (InitialResize < 640 && afterResize >= 640) || (InitialResize >= 640 && afterResize < 640)
        ) {
          InitialResize = afterResize;

          googletag.cmd.push(function() {
            googletag.pubads().refresh();
          });
        }
      }
    });

        googletag.cmd.push(function() {
      window.MomApp = window.MomApp || {};
      window.MomApp.prefetchSlots = window.MomApp.prefetchSlots || {};

      window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-header_desk-377048'] = googletag.defineSlot(
        '/22715092907/ManOfMany/article_1/header_desk', [970,250], 'gam-wrapper__22715092907-manofmany-article_1-header_desk-377048'
      ).defineSizeMapping(
        gamData.sizeMap['headerdesk']
      ).setTargeting(
        'refresh', 'false'
      ).addService(
        googletag.pubads()
      );
    });
        googletag.cmd.push(function() {
      window.MomApp = window.MomApp || {};
      window.MomApp.prefetchSlots = window.MomApp.prefetchSlots || {};

      window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-footer_sticky_desk-377048'] = googletag.defineSlot(
        '/22715092907/ManOfMany/article_1/footer_sticky_desk', [728,90], 'gam-wrapper__22715092907-manofmany-article_1-footer_sticky_desk-377048'
      ).defineSizeMapping(
        gamData.sizeMap['footerdesk']
      ).setTargeting(
        'refresh', 'true'
      ).addService(
        googletag.pubads()
      );
    });
        googletag.cmd.push(function() {
      window.MomApp = window.MomApp || {};
      window.MomApp.prefetchSlots = window.MomApp.prefetchSlots || {};

      window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-header_mob-377048'] = googletag.defineSlot(
        '/22715092907/ManOfMany/article_1/header_mob', [320,50], 'gam-wrapper__22715092907-manofmany-article_1-header_mob-377048'
      ).defineSizeMapping(
        gamData.sizeMap['anchor']
      ).setTargeting(
        'refresh', 'false'
      ).addService(
        googletag.pubads()
      );
    });
        googletag.cmd.push(function() {
      window.MomApp = window.MomApp || {};
      window.MomApp.prefetchSlots = window.MomApp.prefetchSlots || {};

      window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-footer_mob-377048'] = googletag.defineSlot(
        '/22715092907/ManOfMany/article_1/footer_mob', [320,50], 'gam-wrapper__22715092907-manofmany-article_1-footer_mob-377048'
      ).defineSizeMapping(
        gamData.sizeMap['anchor']
      ).setTargeting(
        'refresh', 'false'
      ).addService(
        googletag.pubads()
      );
    });
    
      </script>


<script>(function(w, d, s, l, i) {
        w[l] = w[l] || [];
        w[l].push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
        var f = d.getElementsByTagName(s)[0], j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
        j.async = true;
        j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
        f.parentNode.insertBefore(j, f);
      })(window, document, 'script', 'dataLayer', 'GTM-5LQ4WZW');</script>

<script>
      window.dataLayer = window.dataLayer || [];

      function gtag() {dataLayer.push(arguments);}
    </script>
<script>
      window.dataLayer = window.dataLayer || [];

      
      // GA4 event
      window.dataLayer.push({"event":"article_view_datalayer","postAuthor":"Michael Vane","postTitle":"50+ Best Online Games to Play With Friends","postPublishDate":"2021-07-26","postModifiedDate":"2023-04-15","postTags":"Fortnite,Halo,Nintendo,Nintendo Switch,PC,Playstation,Xbox","postCategories":"Gaming","postCategoryFull":"entertainment\/gaming","postCategoryParent":"entertainment","postYoastScore":80,"postMedicalReviewers":""});
    </script>
<script>
      var staticMetadataObject = {
        type: 'static', //Required: the same for every static asset
        assetid: '/entertainment/gaming/best-online-games-to-play-with-friends', //Required and needs to be unique per asset
        section: 'entertainment', //Required: please discuss values with Nielsen
      };

      var nSdkInstance = NOLBUNDLE.nlsQ('P9CA9AB45-D312-4392-BF72-73F93CBE6A04', 'nSdkInstance', {});
      nSdkInstance.ggPM('staticstart', staticMetadataObject);
    </script>
<style type="text/css" id="wp-custom-css">
			.logged-in .main-slider.owl-carousel.owl-drag .owl-item .image{
	    padding-bottom: 50%;
}		</style>
<noscript><style id="rocket-lazyload-nojs-css">.rll-youtube-player, [data-lazy-src]{display:none !important;}</style></noscript></head>
<body class="post-template-default single single-post postid-377048 single-format-standard">
<div id="gam-wrapper__22715092907-manofmany-article_1-oop-64ded1071159d">
<script type="text/javascript">
      googletag.cmd.push(function() {
        googletag.defineOutOfPageSlot(
          '/22715092907/ManOfMany/article_1/oop', 'gam-wrapper__22715092907-manofmany-article_1-oop-64ded1071159d'
        ).setTargeting(
          'refresh', 'false'
        ).addService(
          googletag.pubads()
        );

        googletag.display('gam-wrapper__22715092907-manofmany-article_1-oop-64ded1071159d');
      });
    </script>
</div>
<div class="mom-ads__1x1">
<div class="mom-ads__inner" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608) + 0px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/1x1', [1,1], 'gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608'
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608:300px}}            @media screen and (min-width:768px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608:90px}}            @media screen and (min-width:992px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-1x1-64ded10711608:250px}}          </style>
</div>
</div>
<header id="masterhead" class="site-header">
<div id="navbar" class="navbar clearfix">
<div class="wrapper">
<div class="icon-box">
<div class="social" style="justify-content:flex-start;">
<div class="m-menu-icon">
<a href="#" onclick="return false" style="color:transparent;text-indent:-9999px;overflow:hidden;">
<div class="icon">Toggle Menu</div>
</a>
</div>
<a href="https://shop.manofmany.com/" rel="noopener" target="_blank" class="m-cart-link"><img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2025%2025'%3E%3C/svg%3E" width="25" height="25" alt="Cart" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/bag.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/bag.svg" width="25" height="25" alt="Cart"></noscript> <span class="m-cart-link__label">SHOP</span></a>
<a href="#" onclick="MomApp.toggleSideMenu({focusSearch: true}); return false;" class="m-cart-link show-on-mobile"><img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Search" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/icon-search-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/icon-search-w.svg" width="20" height="20" alt="Search"></noscript> <span class="m-cart-link__label">Search</span></a>
</div>
<div class="m-logo-icon mom-header-logo">
<a href="https://manofmany.com">
<img src="https://manofmany.com/wp-content/themes/manofmany/images/logo.svg" width="325" height="29" alt="Man of Many" class="mom-header-logo__full">
</a>
</div>
<div class="social">
<div class="site-header__cta">
<div class="invite"><a href="#" onclick="MomApp.triggerNewsletterBoxPopup();return false;"><span>Subscribe</span></a></div>
<div class="mom-share-dropdown">
<button class="mom-share-dropdown__toggle ">
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" width="1em" height="1em" data-component="ShareWeb" class="_1_xkG _35hyT">
<path fill="currentColor" fill-rule="evenodd" d="M15 13s-9-1-12.998 7c0 0 0-13 12.998-13V3l7 7-7 7v-4z" clip-rule="evenodd"></path>
</svg>
Share
</button>
<div data-cmp="share" style="display:none;">
<button class="mom-share-dropdown__close mom-share-dropdown__toggle"><img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" alt="Close" width="15" height="15" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/icon-close-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/icon-close-w.svg" alt="Close" loading="lazy" width="15" height="15"></noscript></button>
<div class="shareicon clearfix">
<p>Share this on</p>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="facebook" class="item st-custom-button share-click"><img alt="Facebook share" title="Facebook" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-fb-b.svg"><noscript><img loading="lazy" alt="Facebook share" title="Facebook" src="https://manofmany.com/wp-content/themes/manofmany/images/soc-fb-b.svg" width="20" height="20"></noscript> Facebook</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="twitter" class="item st-custom-button share-click" data-username="manofmany"><img alt="Twitter share" title="Tweet" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-tw-b.svg"><noscript><img loading="lazy" alt="Twitter share" title="Tweet" src="https://manofmany.com/wp-content/themes/manofmany/images/soc-tw-b.svg" width="20" height="20"></noscript> Twitter</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="linkedin" class="item st-custom-button share-click"><img alt="LinkedIn share" title="LinkedIn" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2018%2020'%3E%3C/svg%3E" width="18" height="20" style="margin-right:7px !important;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/linkedin-b.svg"><noscript><img loading="lazy" alt="LinkedIn share" title="LinkedIn" src="https://manofmany.com/wp-content/themes/manofmany/images/linkedin-b.svg" width="18" height="20" style="margin-right:7px !important;"></noscript> LinkedIn</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="reddit" class="item st-custom-button share-click"><img alt="Reddit share" title="Reddit+" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/reddit-b.svg"><noscript><img loading="lazy" alt="Reddit share" title="Reddit+" src="https://manofmany.com/wp-content/themes/manofmany/images/reddit-b.svg" width="20" height="20"></noscript> Reddit</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="pinterest" class="item st-custom-button share-click"><img alt="Pinterest share" title="Pinterest" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/pinterest-b.svg"><noscript><img loading="lazy" alt="Pinterest share" title="Pinterest" src="https://manofmany.com/wp-content/themes/manofmany/images/pinterest-b.svg" width="20" height="20"></noscript> Pinterest</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="flipboard" class="item st-custom-button share-click"><img alt="Flipboard share" title="Flipboard" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2017%2020'%3E%3C/svg%3E" width="17" height="20" style="margin-right:8px !important;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/flipboard-b.svg"><noscript><img loading="lazy" alt="Flipboard share" title="Flipboard" src="https://manofmany.com/wp-content/themes/manofmany/images/flipboard-b.svg" width="17" height="20" style="margin-right:8px !important;"></noscript> Flipboard</div>
</div>
<div class="shareicon clearfix">
<p style="margin-top:15px;">Send this by</p>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="email" class="item st-custom-button share-click"><img alt="Email share" title="Email" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/email-b.svg"><noscript><img loading="lazy" alt="Email share" title="Email" src="https://manofmany.com/wp-content/themes/manofmany/images/email-b.svg" width="20" height="20"></noscript> Email</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="messenger" class="item st-custom-button share-click"><img alt="Messenger share" title="Messenger" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/messenger-bl.svg"><noscript><img loading="lazy" alt="Messenger share" title="Messenger" src="https://manofmany.com/wp-content/themes/manofmany/images/messenger-bl.svg" width="20" height="20"></noscript> Messenger</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="whatsapp" class="item st-custom-button share-click"><img alt="WhatsApp share" title="Whatsapp" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/whatsapp-b.svg"><noscript><img loading="lazy" alt="WhatsApp share" title="Whatsapp" src="https://manofmany.com/wp-content/themes/manofmany/images/whatsapp-b.svg" width="20" height="20"></noscript> WhatsApp</div>
<div class="item st-custom-button st-custom-button-copy share-click"><img class="st-custom-button-copy__icon--default" alt="Copy link" title="Copy link" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" style="vertical-align:-2px;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/link-b.svg"><noscript><img class="st-custom-button-copy__icon--default" loading="lazy" alt="Copy link" title="Copy link" src="https://manofmany.com/wp-content/themes/manofmany/images/link-b.svg" width="15" height="15" style="vertical-align:-2px;"></noscript>
<img class="st-custom-button-copy__icon--copied" alt="Check" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" style="vertical-align:-2px;display:none;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/check-b.svg"><noscript><img class="st-custom-button-copy__icon--copied" loading="lazy" alt="Check" src="https://manofmany.com/wp-content/themes/manofmany/images/check-b.svg" width="15" height="15" style="vertical-align:-2px;display:none;"></noscript>
<span data-copied="Link copied" data-default="Copy Link" class="st-custom-button-copy__text">Copy Link</span>
</div>
</div>
</div>
</div>
</div>
<div class="m-search-icon">
<a href="#" onclick="return false;" style="color:transparent;text-indent:-9999px;overflow:hidden;">
<div class="icon">Search</div>
</a>
</div>
</div>
</div>
</div>
</div>

<div data-cmp="mobile-menu" class="clearfix">
<div class="mobile-menu">
<div class="mom-mobile-menu__top-bar">
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2032%2032'%3E%3C/svg%3E" width="32" height="32" alt="Man of Many" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/logo-footer-w.svg" /><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/logo-footer-w.svg" width="32" height="32" alt="Man of Many"/></noscript>
<button onclick="MomApp.toggleSideMenu(); return false;" class="mom-mobile-menu__close">X</button>
</div>
<div class="mom-mobile-menu__search-form">
<form role="search" method="get" class="searchform" action="https://manofmany.com/">
<div class="search-box">
<label class="screen-reader-text" for="search-64ded1071462a"><img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2040%2040'%3E%3C/svg%3E" width="40" height="40" alt="Search" class="mom-search-icon" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/search-big-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/search-big-w.svg" width="40" height="40" alt="Search" class="mom-search-icon"></noscript></label>
<input type="search" value="" name="s" class="s" id="search-64ded1071462a" placeholder="Search Man of Many" />
<input type="submit" class="searchsubmit" value="Go" />
</div>
</form>
</div>
<div class="topmenu">
<ul id="menu-main-menu" class="menu"><li id="menu-item-528605" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-528605"><a target="_blank" rel="noopener" href="https://shop.manofmany.com/">Visit Man of Many Shop <span style="color:#004ff2;">(New)</span></a></li>
<li id="menu-item-5" class="home menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-5"><a href="https://manofmany.com/">Home</a></li>
<li id="menu-item-426999" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-426999"><a href="https://manofmany.com/news">News</a></li>
<li id="menu-item-164186" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-164186"><a href="https://manofmany.com/tech">Tech</a>
<ul class="sub-menu">
<li id="menu-item-163303" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163303"><a href="https://manofmany.com/tech/apple">Apple</a></li>
<li id="menu-item-163304" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163304"><a href="https://manofmany.com/tech/audio">Audio</a></li>
<li id="menu-item-163305" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163305"><a href="https://manofmany.com/tech/cameras">Cameras</a></li>
<li id="menu-item-163306" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163306"><a href="https://manofmany.com/tech/computers">Computers</a></li>
<li id="menu-item-163307" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163307"><a href="https://manofmany.com/tech/smartphones">Smartphones</a></li>
<li id="menu-item-163308" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163308"><a href="https://manofmany.com/tech/tvs">TVs</a></li>
</ul>
</li>
<li id="menu-item-164187" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-164187"><a href="https://manofmany.com/fashion">Fashion</a>
<ul class="sub-menu">
<li id="menu-item-164189" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164189"><a href="https://manofmany.com/fashion/mens-fashion-advice">Men&#8217;s Fashion Advice</a></li>
<li id="menu-item-164190" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164190"><a href="https://manofmany.com/fashion/mens-fashion-trends">Men&#8217;s Fashion Trends</a></li>
<li id="menu-item-164191" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164191"><a href="https://manofmany.com/fashion/mens-fragrances">Men&#8217;s Fragrances</a></li>
<li id="menu-item-164192" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164192"><a href="https://manofmany.com/fashion/mens-hairstyles">Men&#8217;s Hairstyles</a></li>
<li id="menu-item-164193" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164193"><a href="https://manofmany.com/fashion/sneakers">Sneakers &amp; Shoes</a></li>
<li id="menu-item-164194" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164194"><a href="https://manofmany.com/fashion/watches">Watches</a></li>
</ul>
</li>
<li id="menu-item-164213" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-164213"><a href="https://manofmany.com/rides">Rides</a>
<ul class="sub-menu">
<li id="menu-item-164214" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164214"><a href="https://manofmany.com/rides/boats">Boats</a></li>
<li id="menu-item-164215" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164215"><a href="https://manofmany.com/rides/cars">Cars</a></li>
<li id="menu-item-164216" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164216"><a href="https://manofmany.com/rides/cycling">Cycling</a></li>
<li id="menu-item-164217" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164217"><a href="https://manofmany.com/rides/flying">Flying</a></li>
<li id="menu-item-164218" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164218"><a href="https://manofmany.com/rides/motorcycles">Motorcycles</a></li>
</ul>
</li>
<li id="menu-item-164195" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-164195"><a href="https://manofmany.com/lifestyle">Lifestyle</a>
<ul class="sub-menu">
<li id="menu-item-164196" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164196"><a href="https://manofmany.com/lifestyle/advice">Advice</a></li>
<li id="menu-item-164197" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164197"><a href="https://manofmany.com/lifestyle/drinks">Drinks</a></li>
<li id="menu-item-164199" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164199"><a href="https://manofmany.com/lifestyle/fitness">Fitness</a></li>
<li id="menu-item-497170" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-497170"><a href="https://manofmany.com/lifestyle/finance">Finance</a></li>
<li id="menu-item-164200" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164200"><a href="https://manofmany.com/lifestyle/food">Food</a></li>
<li id="menu-item-164188" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164188"><a href="https://manofmany.com/lifestyle/grooming">Grooming</a></li>
<li id="menu-item-164201" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164201"><a href="https://manofmany.com/lifestyle/sex-dating">Sex &amp; Dating</a></li>
<li id="menu-item-164202" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164202"><a href="https://manofmany.com/lifestyle/travel">Travel</a></li>
</ul>
</li>
<li id="menu-item-163290" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor menu-item-has-children menu-item-163290"><a href="https://manofmany.com/entertainment">Entertainment</a>
<ul class="sub-menu">
<li id="menu-item-163291" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163291"><a href="https://manofmany.com/entertainment/art">Art</a></li>
<li id="menu-item-163292" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163292"><a href="https://manofmany.com/entertainment/books">Books</a></li>
<li id="menu-item-163293" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-163293"><a href="https://manofmany.com/entertainment/gaming">Gaming</a></li>
<li id="menu-item-163294" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163294"><a href="https://manofmany.com/entertainment/movies-tv">Movies &amp; TV</a></li>
<li id="menu-item-163295" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163295"><a href="https://manofmany.com/entertainment/music">Music</a></li>
<li id="menu-item-163296" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-163296"><a href="https://manofmany.com/entertainment/sport">Sport</a></li>
</ul>
</li>
<li id="menu-item-164203" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-164203"><a href="https://manofmany.com/living">Living</a>
<ul class="sub-menu">
<li id="menu-item-164204" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164204"><a href="https://manofmany.com/living/appliances">Appliances</a></li>
<li id="menu-item-164205" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164205"><a href="https://manofmany.com/living/architecture">Architecture</a></li>
<li id="menu-item-164206" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164206"><a href="https://manofmany.com/living/furniture">Furniture</a></li>
<li id="menu-item-164207" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164207"><a href="https://manofmany.com/living/homewares">Homewares</a></li>
</ul>
</li>
<li id="menu-item-164208" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-164208"><a href="https://manofmany.com/outdoors">Outdoors</a>
<ul class="sub-menu">
<li id="menu-item-164209" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164209"><a href="https://manofmany.com/outdoors/camping">Camping</a></li>
<li id="menu-item-164211" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164211"><a href="https://manofmany.com/outdoors/snow">Snow</a></li>
<li id="menu-item-164212" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164212"><a href="https://manofmany.com/outdoors/surf">Surf</a></li>
</ul>
</li>
</ul> </div>
<div data-cmp="newsletter" class="newsletter clearfix">
<div class="title">
Want to join our exclusive community?
</div>
<form class="invite" method="POST">
<input type="email" placeholder="Enter your email" name="email" class="address" autocomplete="email" />
<button type="submit" name="submit">Subscribe</button>
<span class="result"></span>
</form>
</div>
<div class="social">
<ul class="links menu">
<li>
<a href="https://www.facebook.com/manofmany" rel="noopener" target="_blank">
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Facebook" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-fb-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/soc-fb-w.svg" width="20" height="20" alt="Facebook"></noscript>
</a>
</li>
<li>
<a href="https://twitter.com/manofmany" rel="noopener" target="_blank">
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Twitter" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-tw-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/soc-tw-w.svg" width="20" height="20" alt="Twitter"></noscript>
</a>
</li>
<li>
<a href="https://www.instagram.com/manofmany" rel="noopener" target="_blank">
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Instagram" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-ig-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/soc-ig-w.svg" width="20" height="20" alt="Instagram"></noscript>
</a>
</li>
<li>
<a href="https://www.youtube.com/@manofmany" rel="noopener" target="_blank">
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Youtube" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-yt-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/soc-yt-w.svg" width="20" height="20" alt="Youtube"></noscript>
</a>
</li>
<li>
<a href="https://www.tiktok.com/@manofmany" rel="noopener" target="_blank">
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Tiktok" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/tiktok-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/tiktok-w.svg" width="20" height="20" alt="Tiktok"></noscript>
</a>
</li>
<li>
<a href="https://news.google.com/publications/CAAqBwgKMOif8gow6obQAg?hl=en-AU&gl=AU&ceid=AU%3Aen" rel="noopener" target="_blank">
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="RSS" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/Google-News-png.png"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/Google-News-png.png" width="20" height="20" alt="RSS"></noscript>
</a>
</li>
<li><a href="https://www.linkedin.com/company/2918343/admin/" rel="noopener" target="_blank"> <img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Linkedin" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/iconmonstr-linkedin-1-240.png"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/iconmonstr-linkedin-1-240.png" width="20" height="20" alt="Linkedin"></noscript>
</a></li>
<li>
<a href="https://www.reddit.com/user/manofmanytastes" rel="noopener" target="_blank">
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Reddit" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/reddit-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/reddit-w.svg" width="20" height="20" alt="Reddit"></noscript>
</a>
</li>
<li><a href="https://www.pinterest.com/manofmany" rel="noopener" target="_blank"> <img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" alt="Pinterest" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/pinterest-icon.png"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/pinterest-icon.png" width="20" height="20" alt="Pinterest"></noscript>
</a></li> </ul>
</div>
<div class="footermenu">
<div class="menu clearfix"><ul id="menu-footerleft" class="menu"><li id="menu-item-163310" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-163310"><a href="https://manofmany.com/about">About Us</a></li>
<li id="menu-item-163311" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-163311"><a href="https://manofmany.com/advertising">Advertise With Us</a></li>
<li id="menu-item-528606" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-528606"><a target="_blank" rel="noopener" href="https://shop.manofmany.com/">Man of Many Shop</a></li>
<li id="menu-item-493055" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-493055"><a href="https://manofmany.com/team">Meet the Team</a></li>
<li id="menu-item-493058" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-493058"><a href="https://manofmany.com/awards">Industry Awards</a></li>
<li id="menu-item-422395" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-422395"><a href="https://manofmany.com/press">In the Press</a></li>
<li id="menu-item-422396" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-422396"><a href="https://manofmany.com/contact">Contact Us</a></li>
</ul></div><div class="menu clearfix"><ul id="menu-footerright" class="menu"><li id="menu-item-422397" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-422397"><a href="https://manofmany.com/editorial-policy">Editorial Policy</a></li>
<li id="menu-item-493085" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-493085"><a href="https://manofmany.com/corrections-policy">Corrections Policy</a></li>
<li id="menu-item-493120" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-493120"><a href="https://manofmany.com/fact-checking-policy">Fact-Checking Policy</a></li>
<li id="menu-item-422398" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-privacy-policy menu-item-422398"><a rel="privacy-policy" href="https://manofmany.com/privacy-policy">Privacy Policy</a></li>
<li id="menu-item-163314" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-163314"><a href="https://manofmany.com/terms">Terms and Conditions</a></li>
<li id="menu-item-381363" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-381363"><a href="https://manofmany.com/subscription">Manage Subscription</a></li>
</ul></div> </div>
</div>
</div>
</header>
<div id="viewport">
<div id="search" class="mom-search__popup">
<div class="wrapper">
<form role="search" method="get" class="searchform" action="https://manofmany.com/">
<div class="search-box">
<label class="screen-reader-text" for="search-64ded10731141"><img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2040%2040'%3E%3C/svg%3E" width="40" height="40" alt="Search" class="mom-search-icon" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/search-big-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/search-big-w.svg" width="40" height="40" alt="Search" class="mom-search-icon"></noscript></label>
<input type="search" value="" name="s" class="s" id="search-64ded10731141" placeholder="Search Man of Many" />
<input type="submit" class="searchsubmit" value="Go" />
</div>
</form>
</div>
</div>
<div id="main">
<div class="single post-context " data-section-name="gaming" data-section-top-name="entertainment" data-next-url="https://manofmany.com/fashion/watches/the-beast-returns-with-audemars-piguets-30th-anniversary-royal-oak-offshore" data-next-id="530672" data-this-url="https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends" data-this-id="377048">
<div id="primary" class="content-area normal-post">
<div id="content" class="site-content" role="main">
<div class="mom-banner mom-banner--desktop mom-banner--desktop-2">
<a href="https://manofmany.com/tag/gift-ideas"> <img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201180%2090'%3E%3C/svg%3E" alt="Man of Many Fathers Day Gift Guide Banner" width="1180" height="90" style="width:100%;height:auto;display:block;" data-lazy-src="https://manofmany.com/wp-content/uploads/2023/08/1180x90.jpeg"><noscript><img src="https://manofmany.com/wp-content/uploads/2023/08/1180x90.jpeg" alt="Man of Many Fathers Day Gift Guide Banner" width="1180" height="90" style="width:100%;height:auto;display:block;"></noscript>
</a> </div>
<div class="mom-banner mom-banner--mobile mom-banner--mobile-1">
<a href="https://manofmany.com/tag/gift-ideas"> <img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20778%20150'%3E%3C/svg%3E" alt="Man of Many Fathers Day Gift Guide Banner" width="778" height="150" style="width:100%;height:auto;display:block;" data-lazy-src="https://manofmany.com/wp-content/uploads/2023/08/778x150.jpeg"><noscript><img src="https://manofmany.com/wp-content/uploads/2023/08/778x150.jpeg" alt="Man of Many Fathers Day Gift Guide Banner" width="778" height="150" style="width:100%;height:auto;display:block;"></noscript>
</a> </div>
<article id="post-377048" class="wrapper clearfix post-377048 post type-post status-publish format-standard has-post-thumbnail hentry category-gaming tag-fortnite tag-halo tag-nintendo tag-nintendo-switch tag-pc tag-playstation tag-xbox">
<div data-cmp="share" class="comp-share-sticky-buttons">
<div class="comp-share-sticky-buttons__wrapper">
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="facebook" class="comp-share-sticky-buttons__button st-custom-button share-click" style="background-color:#4267B2;">
<img alt="Facebook share" title="Share on Facebook" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-fb-b.svg"><noscript><img loading="lazy" alt="Facebook share" title="Share on Facebook" src="https://manofmany.com/wp-content/themes/manofmany/images/soc-fb-b.svg" width="15" height="15"></noscript>
</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="twitter" class="comp-share-sticky-buttons__button st-custom-button share-click" data-username="manofmany" style="background-color:#1DA1F2;">
<img alt="Twitter share" title="Share on Tweet" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-tw-b.svg"><noscript><img loading="lazy" alt="Twitter share" title="Share on Tweet" src="https://manofmany.com/wp-content/themes/manofmany/images/soc-tw-b.svg" width="15" height="15"></noscript>
</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="email" class="comp-share-sticky-buttons__button st-custom-button share-click" style="background-color:#FF7B00;">
<img alt="Email share" title="Share via Email" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/email-b.svg"><noscript><img loading="lazy" alt="Email share" title="Share via Email" src="https://manofmany.com/wp-content/themes/manofmany/images/email-b.svg" width="15" height="15"></noscript>
</div>
<div class="comp-share-sticky-buttons__button st-custom-button st-custom-button-copy share-click" style="background-color:#ef5532;">
<img class="st-custom-button-copy__icon--default" alt="Copy link" title="Copy link" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" style="vertical-align:-2px;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/link-b.svg"><noscript><img class="st-custom-button-copy__icon--default" loading="lazy" alt="Copy link" title="Copy link" src="https://manofmany.com/wp-content/themes/manofmany/images/link-b.svg" width="15" height="15" style="vertical-align:-2px;"></noscript>
<img class="st-custom-button-copy__icon--copied" alt="Check" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" style="vertical-align:-2px;display:none;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/check-b.svg"><noscript><img class="st-custom-button-copy__icon--copied" loading="lazy" alt="Check" src="https://manofmany.com/wp-content/themes/manofmany/images/check-b.svg" width="15" height="15" style="vertical-align:-2px;display:none;"></noscript>
<span data-copied="Link copied" data-default="Copy Link" class="st-custom-button-copy__text">Copy Link</span>
</div>
</div>
</div>
<div class="bread-wrap bread-wrap--standard mom-display-only--desktop">
<div id="breadcrumbs" class="breadcrumbs--yoast"><span><span><a href="https://manofmany.com/">Home</a></span> <span class="separator"> &gt; </span> <span><a href="https://manofmany.com/entertainment">Entertainment</a></span> <span class="separator"> &gt; </span> <span><a href="https://manofmany.com/entertainment/gaming">Gaming</a></span></span></div> </div>
<div class="entry-content entry-content--flex small-post clearfix" data-cmp="post-content">
<div class="l-box">
<header class="entry-header entry-header--small">
<div class="post-image-new">
<div class="img-block">
<div class="img-share-block">
<img width="1067" height="800" loading="eager" fetchpriority="high" src="https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends-1067x800.jpg" alt="1 best online games to play with friends" class="alignnone size-full wp-image" sizes="(max-width: 1067px) 100vw, 1067px" srcset="https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends-1067x800.jpg 1067w, https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends-356x267.jpg 356w, https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends-768x576.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg 1200w" />
</div>
</div>
</div>
<div class="cat-names">
<a href="https://manofmany.com/entertainment/gaming">Gaming</a> </div>
<div class="bread-wrap mom-display-only--mobile">
<div id="breadcrumbs" class="breadcrumbs--yoast"><span><span><a href="https://manofmany.com/">Home</a></span> <span class="separator"> &gt; </span> <span><a href="https://manofmany.com/entertainment">Entertainment</a></span> <span class="separator"> &gt; </span> <span><a href="https://manofmany.com/entertainment/gaming">Gaming</a></span></span></div> </div>
<h1 style="margin-top:0" class="entry-title">50+ Best Online Games to Play With Friends</h1>
<div class="border"></div>
<div class="entry-meta clearfix">
<p class="post-info">
By <a href="https://manofmany.com/author/michaelvane">Michael Vane</a> - Guide
<span class="mom-post-dates">
Published: <time class="updated" datetime="2021-07-26T09:00:26+10:00">26 Jul 2021</time>, Last Updated: <time class="updated" datetime="2023-04-15T14:07:34+10:00">15 Apr 2023</time> </span>
</p>
<div class="mom-entry-meta-buttons">
<div data-cmp="share" class="mom-copy-link">
<button class="mom-btn mom-btn--orange st-custom-button-copy share-click">
<img class="st-custom-button-copy__icon--default" alt="Copy link" title="Copy link" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" style="vertical-align:-2px;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/link-b.svg"><noscript><img class="st-custom-button-copy__icon--default" loading="lazy" alt="Copy link" title="Copy link" src="https://manofmany.com/wp-content/themes/manofmany/images/link-b.svg" width="15" height="15" style="vertical-align:-2px;"></noscript>
<img class="st-custom-button-copy__icon--copied" alt="Check" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" style="vertical-align:-2px;display:none;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/check-b.svg"><noscript><img class="st-custom-button-copy__icon--copied" loading="lazy" alt="Check" src="https://manofmany.com/wp-content/themes/manofmany/images/check-b.svg" width="15" height="15" style="vertical-align:-2px;display:none;"></noscript>
<span data-copied="Link copied" data-default="Copy Link" class="st-custom-button-copy__text">Copy Link</span>
</button>
</div>
<div class="mom-share-dropdown">
<button class="mom-share-dropdown__toggle mom-btn mom-btn--orange-outline">
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" width="1em" height="1em" data-component="ShareWeb" class="_1_xkG _35hyT">
<path fill="currentColor" fill-rule="evenodd" d="M15 13s-9-1-12.998 7c0 0 0-13 12.998-13V3l7 7-7 7v-4z" clip-rule="evenodd"></path>
</svg>
Share
</button>
<div data-cmp="share" style="display:none;">
<button class="mom-share-dropdown__close mom-share-dropdown__toggle"><img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" alt="Close" width="15" height="15" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/icon-close-w.svg"><noscript><img src="https://manofmany.com/wp-content/themes/manofmany/images/icon-close-w.svg" alt="Close" loading="lazy" width="15" height="15"></noscript></button>
<div class="shareicon clearfix">
<p>Share this on</p>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="facebook" class="item st-custom-button share-click"><img alt="Facebook share" title="Facebook" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-fb-b.svg"><noscript><img loading="lazy" alt="Facebook share" title="Facebook" src="https://manofmany.com/wp-content/themes/manofmany/images/soc-fb-b.svg" width="20" height="20"></noscript> Facebook</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="twitter" class="item st-custom-button share-click" data-username="manofmany"><img alt="Twitter share" title="Tweet" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/soc-tw-b.svg"><noscript><img loading="lazy" alt="Twitter share" title="Tweet" src="https://manofmany.com/wp-content/themes/manofmany/images/soc-tw-b.svg" width="20" height="20"></noscript> Twitter</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="linkedin" class="item st-custom-button share-click"><img alt="LinkedIn share" title="LinkedIn" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2018%2020'%3E%3C/svg%3E" width="18" height="20" style="margin-right:7px !important;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/linkedin-b.svg"><noscript><img loading="lazy" alt="LinkedIn share" title="LinkedIn" src="https://manofmany.com/wp-content/themes/manofmany/images/linkedin-b.svg" width="18" height="20" style="margin-right:7px !important;"></noscript> LinkedIn</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="reddit" class="item st-custom-button share-click"><img alt="Reddit share" title="Reddit+" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/reddit-b.svg"><noscript><img loading="lazy" alt="Reddit share" title="Reddit+" src="https://manofmany.com/wp-content/themes/manofmany/images/reddit-b.svg" width="20" height="20"></noscript> Reddit</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="pinterest" class="item st-custom-button share-click"><img alt="Pinterest share" title="Pinterest" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/pinterest-b.svg"><noscript><img loading="lazy" alt="Pinterest share" title="Pinterest" src="https://manofmany.com/wp-content/themes/manofmany/images/pinterest-b.svg" width="20" height="20"></noscript> Pinterest</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="flipboard" class="item st-custom-button share-click"><img alt="Flipboard share" title="Flipboard" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2017%2020'%3E%3C/svg%3E" width="17" height="20" style="margin-right:8px !important;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/flipboard-b.svg"><noscript><img loading="lazy" alt="Flipboard share" title="Flipboard" src="https://manofmany.com/wp-content/themes/manofmany/images/flipboard-b.svg" width="17" height="20" style="margin-right:8px !important;"></noscript> Flipboard</div>
</div>
<div class="shareicon clearfix">
<p style="margin-top:15px;">Send this by</p>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="email" class="item st-custom-button share-click"><img alt="Email share" title="Email" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/email-b.svg"><noscript><img loading="lazy" alt="Email share" title="Email" src="https://manofmany.com/wp-content/themes/manofmany/images/email-b.svg" width="20" height="20"></noscript> Email</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="messenger" class="item st-custom-button share-click"><img alt="Messenger share" title="Messenger" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/messenger-bl.svg"><noscript><img loading="lazy" alt="Messenger share" title="Messenger" src="https://manofmany.com/wp-content/themes/manofmany/images/messenger-bl.svg" width="20" height="20"></noscript> Messenger</div>
<div data-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-title=50+ Best Online Games to Play With Friends data-share-url=https://manofmany.com/entertainment/gaming/best-online-games-to-play-with-friends data-image=https://manofmany.com/wp-content/uploads/2021/07/1-Best-Online-Games-to-Play-With-Friends.jpg data-network="whatsapp" class="item st-custom-button share-click"><img alt="WhatsApp share" title="Whatsapp" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E" width="20" height="20" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/whatsapp-b.svg"><noscript><img loading="lazy" alt="WhatsApp share" title="Whatsapp" src="https://manofmany.com/wp-content/themes/manofmany/images/whatsapp-b.svg" width="20" height="20"></noscript> WhatsApp</div>
<div class="item st-custom-button st-custom-button-copy share-click"><img class="st-custom-button-copy__icon--default" alt="Copy link" title="Copy link" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" style="vertical-align:-2px;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/link-b.svg"><noscript><img class="st-custom-button-copy__icon--default" loading="lazy" alt="Copy link" title="Copy link" src="https://manofmany.com/wp-content/themes/manofmany/images/link-b.svg" width="15" height="15" style="vertical-align:-2px;"></noscript>
<img class="st-custom-button-copy__icon--copied" alt="Check" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E" width="15" height="15" style="vertical-align:-2px;display:none;" data-lazy-src="https://manofmany.com/wp-content/themes/manofmany/images/check-b.svg"><noscript><img class="st-custom-button-copy__icon--copied" loading="lazy" alt="Check" src="https://manofmany.com/wp-content/themes/manofmany/images/check-b.svg" width="15" height="15" style="vertical-align:-2px;display:none;"></noscript>
<span data-copied="Link copied" data-default="Copy Link" class="st-custom-button-copy__text">Copy Link</span>
</div>
</div>
</div>
</div>
</div>
</div>
</header>
<p>With a near-endless selection of online games and blockbuster titles vying for your time, how do you choose which ones to play? Start with a helpful guide like this, of course! We&#8217;ve scoured the app stores and digital marketplaces to create a comprehensive guide to the best online multiplayer games to play with friends. Some games are popular, while others are still up and coming. There&#8217;s even a few classics in the mix. Whether you&#8217;re looking for free to play games to kill some time or a new virtual life to lose yourself in for 100+ hours, there&#8217;s something for everyone on this list. So without further delay, here&#8217;s our comprehensive guide to the best online games for you and your friends:</p>
<p><strong>You&#8217;ll also like:</strong><br />
<a href="https://manofmany.com/entertainment/movies-tv/scariest-horror-movies-according-to-science">20 Scariest Horror Movies of All Time According to Science</a><br />
<a href="https://manofmany.com/entertainment/gaming/where-to-buy-ps5-australia">Where to Buy a PS5 in Australia: 10 Restock Spots</a><br />
<a href="https://manofmany.com/entertainment/gaming/best-e3-games-2021">10 Best New Games Revealed at E3 2021</a></p>
<h3 id="anchor-60fb82d7f2e73"><img decoding="async" fetchpriority="high" class="alignnone size-full wp-image-374156" title="Best online games destiny 2" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games destiny 2" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2.jpg" /><noscript><img decoding="async" fetchpriority="high" class="alignnone size-full wp-image-374156" title="Best online games destiny 2" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2.jpg" alt="Best online games destiny 2" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-destiny-2-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></h3>
<h3 id="1_Destiny-2">1. Destiny 2</h3>
<p>Team up for one of the best online multiplayer games ever made and explore the galaxy in the ever-expanding action RPG Destiny 2. Launching back in 2017, this looter shooter continues to evolve giving players enough reasons to keep playing or to jump back in after a break. Destiny 2 has even gone free to play, so new players can take to the story in three-player co-op, attempt raids as part of six-man squads and takedown randoms in PvP without spending a cent.</p>
<p><strong>Genre:</strong> Action RPG<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 6</p>
<p><a class="ch_custom" href="https://www.bungie.net/7/en/Destiny/NewLight" target="_blank" rel="noopener">Check it out</a> <div class="comp-jwplayer">
<script src="https://cdn.jwplayer.com/libraries/WMENi2H3.js"></script>
<div id="comp-jwplayer-377048"></div>
<script>
      jwplayer('comp-jwplayer-377048').setup({
        'playlist': "https://cdn.jwplayer.com/v2/playlists/WQg6GrOj",
        'floating': {
          'dismissible': true,
                  },
      });
    </script>
</div>
</p><p><img decoding="async" class="alignnone size-full wp-image-374152" title="Best online games cod warzone" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games cod warzone" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374152" title="Best online games cod warzone" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone.jpg" alt="Best online games cod warzone" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cod-warzone-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_1-64ded10783a49) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_1-64ded10783a49">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_1-64ded10783a49']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_1-64ded10783a49'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_1', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_1-64ded10783a49'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_1-64ded10783a49');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_1-64ded10783a49:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_1-64ded10783a49:90px}}          </style>
</div>
</div>
<h3 id="2_Call-of-duty:-warzone">2. Call of Duty: Warzone</h3>
<p>One of the newest faces on the battle royale scene, Call of Duty: Warzone is a free-to-play online multiplayer game for up to 150 players who parachute in, armour up, loot for rewards, and fight to be part of the last squad standing. It’s the same Call of Duty action you know and love, scaled up with huge maps, vehicles, unique operators and multiple modes that change across seasons. Warzone supports crossplay, meaning you and your friends can squad up no matter how or where you play video games.</p>
<p><strong>Genre:</strong> Battle Royale<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S XB1<br />
<strong>Squad size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.callofduty.com/au/en/warzone" target="_blank" rel="noopener">Check it out</a>
<div data-cmp="newsletter" class="comp-newsletter-box comp-newsletter-box--layout-post-content">
<div class="comp-newsletter-box__inner">
<div class="comp-newsletter-box__content">
<div class="comp-newsletter-box__title">
Join Our Exclusive Community!
</div>
<div class="comp-newsletter-box__description">
Keep up with the latest trends, best stories, and crucial updates from Man of Many direct to your inbox.
</div>
<form class="comp-newsletter-box__form invite" method="POST">
<input type="email" placeholder="Enter your email" name="email" class="comp-newsletter-box__form__email address" autocomplete="email" />
<button type="submit" name="submit" class="comp-newsletter-box__form__submit">Subscribe</button>
</form>
<span class="comp-newsletter-box__form-message result"></span>
</div>
</div>
</div>
</p><p><img decoding="async" class="alignnone size-full wp-image-374149" title="Best online games among us" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games among us" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374149" title="Best online games among us" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us.jpg" alt="Best online games among us" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-among-us-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="3_Among-us">3. Among Us</h3>
<p>This indie game launched a few years back although its popularity skyrocketed during the COVID-19 pandemic thanks to the social aspects and free to play nature of the mobile version. Among Us is a game of deduction, where you and a group of players crew a spaceship, but one player is a shapeshifting alien who disrupts your journey home by attempting to murder everyone on board. Once a body is reported, you vote on who’s the culprit. If successful, the killer is ejected into space. If not, the alien is free to carry out further crimes.</p>
<p><strong>Genre:</strong> Social, deduction<br />
<strong>Platforms:</strong> PC, PS4, XB1, Switch, iOS, Android<br />
<strong>Player count:</strong> 4 -15</p>
<p><a class="ch_custom" href="https://innersloth.com/gameAmongUs.php" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374182" title="Best online games sea of thieves" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="sea of thieves" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374182" title="Best online games sea of thieves" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves.jpg" alt="sea of thieves" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-sea-of-thieves-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="4_Sea-of-thieves">4. Sea of Thieves</h3>
<p>A social game at its core, Sea of <a title="100 Thieves eSports Gaming Compound and Training Facility" href="https://manofmany.com/entertainment/gaming/tour-of-100-thieves-esports-gaming-compound-and-training-facility">Thieves is one of the best games</a> to play online. It’s all about teaming up with some scallywags, crewing a ship, seeking buried treasure, fighting skeletons and having a laugh. Your pirate crew can be noble or a bunch of total a-holes, depending on how often you raid and murder the other players online. Set sail, survive the Kraken, fire friends out of cannons and sing a sea shanty or two. Fun times!</p>
<p><strong>Genre:</strong> Social, survival<br />
<strong>Platforms:</strong> PC, XBX/S, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.seaofthieves.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374172" title="Best online games nba 2k20" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games nba 2k20" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374172" title="Best online games nba 2k20" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20.jpg" alt="Best online games nba 2k20" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-nba-2k20-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_2-64ded10783ab9) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_2-64ded10783ab9">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_2-64ded10783ab9']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_2-64ded10783ab9'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_2', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_2-64ded10783ab9'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_2-64ded10783ab9');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_2-64ded10783ab9:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_2-64ded10783ab9:90px}}          </style>
</div>
</div>
<h3 id="5_Nba-2k20">5. NBA 2K20</h3>
<p>The best way to get that baller fix without getting off the couch is with a few pick-up games of NBA 2K20. Or, select your favourite team, play a new season, and maybe you can rise to the level of GOAT. NBA 2k20 has more realistic player controls, advanced shooting, refined collisions and a new dribbling system for the most authentic basketball experience in gaming.</p>
<p><strong>Genre:</strong> Sports<br />
<strong>Platforms:</strong> PC, PS4, XB1, Switch<br />
<strong>Team size:</strong> 1 &#8211; 5</p>
<p><a class="ch_custom" href="https://nba.2k.com/2k20/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone wp-image-374173 size-full" title="Best online games overcooked 2" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="overcooked all you can eat" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2.jpg" /><noscript><img decoding="async" class="alignnone wp-image-374173 size-full" title="Best online games overcooked 2" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2.jpg" alt="overcooked all you can eat" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-overcooked-2-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="6_Overcooked:-all-you-can-eat">6. Overcooked: All You Can Eat</h3>
<p>You and up to three of your friends work together to prepare a bunch of meals within a set time limit. It’s a simple concept that quickly gets out of hand when hazards like bottomless pits, swamps, fires and moving countertops stand in between you and culinary perfection. Whatever the result, hilarity ensues.</p>
<p><strong>Genre:</strong> Party<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1, Switch<br />
<strong>Player count:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.team17.com/introducing-overcooked-all-you-can-eat/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374170" title="Best online games minecraft" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="minecraft" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374170" title="Best online games minecraft" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft.jpg" alt="minecraft" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-minecraft-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="7_Minecraft">7. Minecraft</h3>
<p>There’s a good reason why Minecraft is the second bestselling game of all time. It’s a digital block builder with unlimited potential. A good imagination is required to make the most of this pixelated gem, but there’s no set way to play. You and some friends can build, scavenge and hang out ‘til your heart’s content. You can craft hideouts and defend them against monsters at night. Or, play creative mode and just build inspiring structures to share with other players and show off online.</p>
<p><strong>Genre:</strong> Construction, survival<br />
<strong>Platforms:</strong> PS4, XB1, Switch, PC, iOS, Android<br />
<strong>Player count:</strong> 1 &#8211; 10</p>
<p><a class="ch_custom" href="https://www.minecraft.net/en-us" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374183" title="Best online games smash bros ultimate" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games smash bros ultimate" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374183" title="Best online games smash bros ultimate" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate.jpg" alt="Best online games smash bros ultimate" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-smash-bros-ultimate-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_3-64ded10783b1a) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_3-64ded10783b1a">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_3-64ded10783b1a']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_3-64ded10783b1a'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_3', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_3-64ded10783b1a'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_3-64ded10783b1a');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_3-64ded10783b1a:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_3-64ded10783b1a:90px}}          </style>
</div>
</div>
<h3 id="8_Super-smash-bros-ultimate">8. Super Smash Bros. Ultimate</h3>
<p>Sometimes you want to play alongside your friends while other times you want to destroy them. Super Smash Bros. Ultimate combines over 70 Fighters from Nintendo’s catalogue plus extras like Sonic the Hedgehog, Snake from Metal Gear and Ryu from Street Fighter. Hold a 4-player free-for-all, or kick it up to 8-player battles across 100 plus stages. It’s fast; it’s over the top and overall, one of the best online games.</p>
<p><strong>Genre:</strong> Fighting<br />
<strong>Platform:</strong> Switch<br />
<strong>Player count:</strong> 1 &#8211; 8</p>
<p><a class="ch_custom" href="https://www.smashbros.com/en_AU/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374166" title="Best online games gta online" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="gta online" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374166" title="Best online games gta online" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online.jpg" alt="gta online" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-gta-online-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="9_Gta-online">9. GTA Online</h3>
<p>Despite GTA V launching almost a decade ago, the multiplayer portion of the game goes from strength to strength with a higher player count year on year. GTA Online is a shared social space where you can race, battle and compete against players online right across the Los Santos landscape all while building your criminal empire. Rockstar expands the online experience each year with new content including co-op heists, deathmatch arenas and Hot Wheels-like race tracks. There’s no shortage of things to do, and with a next-gen update arriving soon, it’s never too late to jump in.</p>
<p><strong>Genre:</strong> MMO<br />
<strong>Platforms:</strong> PC, PS4, XB1<br />
<strong>Player count:</strong> 1 &#8211; 30</p>
<p><a class="ch_custom" href="https://www.rockstargames.com/GTAOnline" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374174" title="Best online games path of exile" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games path of exile" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374174" title="Best online games path of exile" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile.jpg" alt="Best online games path of exile" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-path-of-exile-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="10_Path-of-exile">10. Path of Exile</h3>
<p>Diablo III might be the go-to hack-and-slash dungeon crawler for RPG fans, but Path of Exile offers a comparable experience and is free-to-play. From New Zealand developer Grinding Gear Games, players of Path of Exile join forces and fight to survive the dark continent Wraeclast. Create a character, customise them from hundreds of available skills and keep looting for the best and rarest weapons and armour. Path of Exile was good at launch with the constant stream of free expansions making it better and offering more content with each update. A free to play sequel is also expected soon.</p>
<p><strong>Genre:</strong> Action RPG<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Player count:</strong> 1 &#8211; 6</p>
<p><a class="ch_custom" href="https://www.pathofexile.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374162" title="Best online games final fantasy xiv" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="final fantasy xiv realm reborn" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374162" title="Best online games final fantasy xiv" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv.jpg" alt="final fantasy xiv realm reborn" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-final-fantasy-xiv-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_4-64ded10783b82) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_4-64ded10783b82">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_4-64ded10783b82']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_4-64ded10783b82'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_4', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_4-64ded10783b82'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_4-64ded10783b82');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_4-64ded10783b82:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_4-64ded10783b82:90px}}          </style>
</div>
</div>
<h3 id="11_Final-fantasy-xiv:-a-realm-reborn">11. Final Fantasy XIV: A Realm Reborn</h3>
<p>The original Final Fantasy XIV was a huge failure. However, tonnes of new content and a relaunch under the Realm Reborn moniker sees this Final Fantasy grow to become one of the best online games available today. Gaming website IGN even describes Realm Reborn as the absolute best MMO for investing countless hours of your time. Live and breathe Final fantasy as you craft, hunt, socialise, ride Chocobos and become a warrior if light, helping save the realm from certain destruction.</p>
<p><strong>Genre:</strong> MMO<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Party size:</strong> 1 &#8211; 8</p>
<p><a class="ch_custom" href="https://na.finalfantasyxiv.com/a_realm_reborn/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374181" title="Best online games rocket league" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games rocket league" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374181" title="Best online games rocket league" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league.jpg" alt="Best online games rocket league" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-rocket-league-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="12_Rocket-league">12. Rocket League</h3>
<p>Easy to pick up, tough to master, Rocket League combines car racing and FIFA for what is basically a giant game of football played with a beach ball and exploding cars. It’s also one of the best online multiplayer games. In this free to play racer/baller, you customise a vehicle, form a team with friends or join some random players online, then boost, nudge and knock the ball towards the goal net. Simple right? Rocket League has proven so successful that it’s now played for competitive eSports and regularly receives new content, meaning there are always reasons to roll back onto the field.</p>
<p><strong>Genre:</strong> Sports, racing<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1, Switch<br />
<strong>Team size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.rocketleague.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374159" title="Best online games draw something" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="draw something" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374159" title="Best online games draw something" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something.jpg" alt="draw something" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-draw-something-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="13_Draw-something">13. Draw Something</h3>
<p>Draw Something is a free to play digital Pictionary alternative where you and your friends take turns choosing a word and attempting to draw it for the other players to guess. Hilarity ensues as most of us couldn’t draw if our lives depended on it, let alone under the pressures of a time limit and the impending ridicule of your mates. Available via web browser or app, the endless laughs are enough to make Draw Something one of the best online games for mobile.</p>
<p><strong>Genre:</strong> Social<br />
<strong>Platforms:</strong> iOS, Android, web browser<br />
<strong>Player count:</strong> 2 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.zynga.com/games/draw-something/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374161" title="Best online games fall guys" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="fall guys: ultimate knockout" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374161" title="Best online games fall guys" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys.jpg" alt="fall guys: ultimate knockout" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fall-guys-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_5-64ded10783bdf) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_5-64ded10783bdf">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_5-64ded10783bdf']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_5-64ded10783bdf'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_5', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_5-64ded10783bdf'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_5-64ded10783bdf');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_5-64ded10783bdf:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_5-64ded10783bdf:90px}}          </style>
</div>
</div>
<h3 id="14_Fall-guys:-ultimate-knockout">14. Fall Guys: Ultimate Knockout</h3>
<p>One of 2020&#8217;s most popular games was <a href="https://manofmany.com/entertainment/gaming/interview-how-fall-guys-ultimate-knockout-breathes-new-life-into-the-gaming-scene">Fall Guys: Ultimate Knockout</a>. Inspired by balls-out Japanese game shows, this online multiplayer game takes 60 tumbly characters and sets them off down tough as nails obstacle courses, withering away numbers each round until one player is crowned champion. Fall Guys offers a healthy mix of slapstick comedy and competitive chaos with the seasonal events, new courses and costumes giving people plenty of reasons to keep playing well into the game’s second year.</p>
<p><strong>Genre:</strong> Party<br />
<strong>Platforms:</strong> PC, PS4, XB1, Switch<br />
<strong>Player count:</strong> 60</p>
<p><a class="ch_custom" href="https://fallguys.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374154" title="Best online games dead by daylight" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games dead by daylight" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374154" title="Best online games dead by daylight" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight.jpg" alt="Best online games dead by daylight" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-dead-by-daylight-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="15_Dead-by-daylight">15. Dead by Daylight</h3>
<p>Dead by Daylight is the ultimate game for fans of slasher films. It’s an asymmetrical multiplayer experience for 5 players, where four take on the roles of scared survivors looking to escape while the fifth player is the killer, who aims to brutally takedown as many players as possible. Dead by Daylight successfully captures the tension of horror films and features licensing from Silent Hill, Evil Dead, Scream, Nightmare on Elm Street, Stranger Things, Saw and Resident Evil to name drop a few.</p>
<p><strong>Genre:</strong> Multiplayer, horror<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Player count:</strong> 5</p>
<p><a class="ch_custom" href="https://deadbydaylight.com/en" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374189" title="Best online games words with friends 2" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games words with friends 2" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374189" title="Best online games words with friends 2" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2.jpg" alt="Best online games words with friends 2" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-words-with-friends-2-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="16_Words-with-friends-2">16. Words with Friends 2</h3>
<p>Words with Friends 2 is the free to play Scrabble alternative that’s flaunted as the world’s most popular mobile word game. You’ll be unscrambling letters, improving your vocabulary and scoring bragging rights over friends and random players online. There’s also lightning rounds, goals and solo challenges to fill that time on your daily commute. Downloading this one to your phone is a no brainer.</p>
<p><strong>Genre:</strong> Puzzle, social<br />
<strong>Platforms:</strong> iOS, Android<br />
<strong>Player count:</strong> 1 &#8211; 5</p>
<p><a class="ch_custom" href="https://www.zynga.com/games/words-with-friends-2/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374164" title="Best online games forza horizon 4" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="forza horizon 4" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374164" title="Best online games forza horizon 4" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4.jpg" alt="forza horizon 4" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-forza-horizon-4-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_6-64ded10783c3a) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_6-64ded10783c3a">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_6-64ded10783c3a']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_6-64ded10783c3a'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_6', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_6-64ded10783c3a'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_6-64ded10783c3a');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_6-64ded10783c3a:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_6-64ded10783c3a:90px}}          </style>
</div>
</div>
<h3 id="17_Forza-horizon-4">17. Forza Horizon 4</h3>
<p>In Forza Horizon 4, race, drift and stunt your way through a gorgeous recreation of the English countryside while testing over 450 of the world’s most iconic rides. Experience dynamic seasons of weather as you take on the valleys, lakesides and castles throughout the campaign. Then, jump online with some friends or randoms to compete for online prestige. Forza Horizon 4 is an acclaimed racer that will keep you and some mates well entertained. At least until <a href="https://manofmany.com/entertainment/gaming/forza-horizon-5-announcement">Forza Horizon 5</a> arrives in November 2021.</p>
<p><strong>Genre:</strong> Racing<br />
<strong>Platforms:</strong> PC, XBX/S, XB1<br />
<strong>Player count:</strong> 1 &#8211; 6</p>
<p><a class="ch_custom" href="https://forzamotorsport.net/en-US/games/fh4" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374151" title="Best online games apex legends" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games apex legends" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374151" title="Best online games apex legends" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends.jpg" alt="Best online games apex legends" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-apex-legends-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="18_Apex-legends">18. Apex Legends</h3>
<p>Apex Legends combines the gameplay of acclaimed shooter Titanfall 2 with the juvenile humour of Fortnite for a unique battle royale that’s been going strong for a few years now. This free-to-play game can be enjoyed alone but rewards teamwork and playing with others is the best way to become the last squad standing. The humour isn’t for everyone but the gameplay is tight and the typical short length of matches makes it hard to grow tired of this experience.</p>
<p><strong>Genre:</strong> Battle royale, shooter<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1, Switch<br />
<strong>Squad size:</strong> 1- 3</p>
<p><a class="ch_custom" href="https://www.ea.com/games/apex-legends" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374150" title="Best online games animal crossing" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="animal crossing new horizons" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374150" title="Best online games animal crossing" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing.jpg" alt="animal crossing new horizons" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-animal-crossing-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="19_Animal-crossing:-new-horizons">19. Animal Crossing: New Horizons</h3>
<p>Jump into Animal Crossing: New Horizons and your virtual escape couldn&#8217;t be any more wholesome. You&#8217;re the newest resident of an island paradise brimming with possibility. Craft, collect, go fishing and build the ultimate cutesy community. Then, invite real-world friends over to see your island utopia or pack your bags and take a trip to theirs. Launching right at the start of the pandemic, Animal Crossing couldn’t be any more relevant, and it’s undoubtedly one of the best games to play online with friends.</p>
<p><strong>Genre:</strong> social, sim<br />
<strong>Platform:</strong> Switch<br />
<strong>Players:</strong> 1 &#8211; 8</p>
<p><a class="ch_custom" href="https://www.animal-crossing.com/new-horizons/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374188" title="Best online games warframe" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games warframe" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374188" title="Best online games warframe" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe.jpg" alt="Best online games warframe" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-warframe-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_7-64ded10783c96) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_7-64ded10783c96">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_7-64ded10783c96']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_7-64ded10783c96'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_7', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_7-64ded10783c96'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_7-64ded10783c96');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_7-64ded10783c96:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_7-64ded10783c96:90px}}          </style>
</div>
</div>
<h3 id="20_Warframe">20. Warframe</h3>
<p>Tens of millions of people play Warframe for two reasons: It’s free and loads of fun. It’s an online co-op shooter for up to four players. Set in a futuristic alien landscape, players take on the role of Tenno, who are basically space ninjas at war with alien races. Like Destiny, The Division and several other online games, the core gameplay loop involves completing missions, upgrading weapons, armour and abilities and repeating in search of better loot. Warframe is free. There’s absolutely no reason not to give it a go.</p>
<p><strong>Genre:</strong> Action, RPG<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.warframe.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-377055" title="Phantom abyss" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Phantom abyss" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-377055" title="Phantom abyss" src="https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss.jpg" alt="Phantom abyss" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/phantom-abyss-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="21_Phantom-abyss">21. Phantom Abyss</h3>
<p>Phantom Abyss is an Indiana Jones and the Temple of Doom simulator. You traverse hectic temples full of traps to retrieve relics and get further than your friends. It’s an asynchronous multiplayer game, so you and your friends or random players online all compete through the temples at the same time. You can use the other players as a guide or simply collect their whips and use them to your advantage. The procedurally generated temples are unique each run, so no two Phantom Abyss runs will ever be the same.</p>
<p><strong>Genre:</strong> Action, rogue-like<br />
<strong>Platform:</strong> PC<br />
<strong>Player count:</strong> 1 &#8211; 20</p>
<p><a class="ch_custom" href="//store.steampowered.com/app/989440/Phantom_Abyss/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374179" title="Best online games red dead online" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="red dead online" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374179" title="Best online games red dead online" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online.jpg" alt="red dead online" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-red-dead-online-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="22_Red-dead-online">22. Red Dead Online</h3>
<p>Following your 100 or so hours spent conquering the untamed wilderness in Red Dead Redemption 2, there’s plenty more to see and do in Red Dead Online. Deathmatches, horse races, hunting, trading, exploring and a light story keeps you busy while daily challenges and a constant stream of updates means you and your outlaw posse are never short of things to do. It may feel odd that one of the best single-player experiences also makes a list of the best online multiplayer games but Red Dead succeeds at both.</p>
<p><strong>Genre:</strong> MMO, western<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 7</p>
<p><a class="ch_custom" href="https://www.rockstargames.com/reddeadonline/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374169" title="Best online games mario kart 8 deluxe" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games mario kart 8 deluxe" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374169" title="Best online games mario kart 8 deluxe" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe.jpg" alt="Best online games mario kart 8 deluxe" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-mario-kart-8-deluxe-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_8-64ded10783cf0) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_8-64ded10783cf0">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_8-64ded10783cf0']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_8-64ded10783cf0'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_8', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_8-64ded10783cf0'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_8-64ded10783cf0');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_8-64ded10783cf0:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_8-64ded10783cf0:90px}}          </style>
</div>
</div>
<h3 id="23_Mario-kart-8-deluxe">23. Mario Kart 8 Deluxe</h3>
<p>As the king of family-friendly racers, Mario Kart 8 Deluxe is a must-own for Switch and a must player for everyone who has ever considered themselves a gamer. This rowdy racer has thrived across two console generations and continues to dominate thanks to its accessible yet technical racing and beloved characters. So, pick up a Joy-Con and dominate the family in four-player split-screen or jump online and compete against the world’s best players for gaming glory. Just be mindful of the inevitable blue shell!</p>
<p><strong>Genre:</strong> Racing<br />
<strong>Platform:</strong> Switch<br />
<strong>Player count:</strong> 1 &#8211; 12</p>
<p><a class="ch_custom" href="https://www.nintendo.com/games/detail/mario-kart-8-deluxe-switch/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374190" title="Best online games crash team racing" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="crash team racing nitro" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374190" title="Best online games crash team racing" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing.jpg" alt="crash team racing nitro" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-crash-team-racing-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="24_Crash-team-racing:-nitro-fuel">24. Crash Team Racing: Nitro-Fueled</h3>
<p>For everyone who doesn&#8217;t own a Nintendo console, there’s Crash Team Racing. Nitro-Fueled is a remake of the 1999 kart racer. It’s addictive, fast-paced racing for up to four competitive friends seeking bragging rights. Or, there’s always the option of racing against randoms online and placing in the leaderboards to take that bragging to the next level.</p>
<p><strong>Genre:</strong> Racing<br />
<strong>Platforms:</strong> PS4, XB1, Switch<br />
<strong>Player count:</strong> 1- 4</p>
<p><a class="ch_custom" href="https://www.activision.com/au/en/games/crash/crash-team-racing" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374160" title="Best online games elder scrolls online" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="elder scrolls online art" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374160" title="Best online games elder scrolls online" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online.jpg" alt="elder scrolls online art" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-elder-scrolls-online-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="25_The-elder-scrolls-online">25. The Elder Scrolls Online</h3>
<p>If you love Skyrim, then you’ll adore the Elder Scrolls Online. It’s one of the best games to play online if you plan on leaving the real world behind. You and your mates choose a race, class and create a character from scratch before taking on epic quests and generally living your best fantasy life. Raid, pickpocket, fish, hunt, craft, and explore your way through hundreds of hours worth of content playing solo or with a squad of like-minded adventurers. Elder Scrolls Online has received major expansions each year, and recent updates for PS5 and Xbox Series X means this online game is looking better than ever.</p>
<p><strong>Genre:</strong> MMORPG<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Player count:</strong> 1 &#8211; 12</p>
<p><a class="ch_custom" href="https://www.elderscrollsonline.com/en-us/home" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374184" title="Best online games spellbreak" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games spellbreak" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374184" title="Best online games spellbreak" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak.jpg" alt="Best online games spellbreak" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-spellbreak-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_9-64ded10783d4b) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_9-64ded10783d4b">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_9-64ded10783d4b']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_9-64ded10783d4b'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_9', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_9-64ded10783d4b'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_9-64ded10783d4b');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_9-64ded10783d4b:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_9-64ded10783d4b:90px}}          </style>
</div>
</div>
<h3 id="26_Spellbreak">26. Spellbreak</h3>
<p>There’s no shortage of multiplayer shooters out there, which is why Spellbreak is a breath of fresh air. Spellbreak is a classed-based competitive game, but instead of assault rifles and shotguns, players wield magic to takedown opponents, all while traversing gorgeous Zelda-inspired arenas. Play across your choice of battle royale, team deathmatch and Dominion game modes. Choose classes who wield fire, ice, lightning, stone and toxicity to eliminate other players and make use of unique abilities such as levitating, teleportation and turning invisible, all to get the upper hand. Spellbreak could be the most unique shooter of the last few years.</p>
<p><strong>Genre:</strong> Battle Royale, VS<br />
<strong>Platforms:</strong> PC, PS4, XB1, Switch<br />
<strong>Squad size:</strong> 1 &#8211; 3</p>
<p><a class="ch_custom" href="https://go.playspellbreak.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374171" title="Best online games monster hunter world" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="monster hunter world" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374171" title="Best online games monster hunter world" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world.jpg" alt="monster hunter world" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-monster-hunter-world-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="-27_Mnster-hunter-world">27. Monster Hunter World</h3>
<p>This popular franchise hit its peak with 2018’s Monster Hunter World. Teaming up with friends to take down larger than life monsters is a thrilling experience and the promise of bigger and better weapons and armour is what makes continuing worthwhile. Over 16 million players have taken to the living, breathing ecosystem of the New World, and the seasonal events and Iceborne expansion means there’s never a shortage of things to see and do.</p>
<p><strong>Genre:</strong> Action RPG<br />
<strong>Platforms:</strong> PC, PS4, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="http://www.monsterhunterworld.com/us/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374165" title="Best online games golf battle" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games golf battle" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374165" title="Best online games golf battle" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle.jpg" alt="Best online games golf battle" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-golf-battle-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="28_Golf-battle">28. Golf Battle</h3>
<p>This free to play mobile game is easy to learn and allows you to challenge real players from across the globe in rounds of mini-golf. In Golf Battle, form a party up with five friends and engage in six-player mini golf set in real-time. It&#8217;s simple, yet addictive. This game has you covered whether you’re a casual player looking to kill some time or a mobile gaming die-hard chasing all the special club and ball unlocks!</p>
<p><strong>Genre:</strong> Sports<br />
<strong>Platforms:</strong> iOS, Android<br />
<strong>Player count:</strong> 1 &#8211; 6</p>
<p><a class="ch_custom" href="https://apps.apple.com/us/app/golf-battle/id1422866002" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374163" title="Best online games fortnite" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="fortnite art" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374163" title="Best online games fortnite" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite.jpg" alt="fortnite art" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-fortnite-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_10-64ded10783da7) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_10-64ded10783da7">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_10-64ded10783da7']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_10-64ded10783da7'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_10', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_10-64ded10783da7'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_10-64ded10783da7');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_10-64ded10783da7:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_10-64ded10783da7:90px}}          </style>
</div>
</div>
<h3 id="29_Fortnite">29. Fortnite</h3>
<p>The global phenomenon that is Fortnite continues to thrive thanks to its constant stream of new content and pop-culture crossovers. This free to play battle royale offers a great deal of content and variety, whether you’re a gamer who craves victory or a virtual landscape for flossing with your mates. The inclusion of famous faces like Loki, Superman, Rick and Morty and Lebron James keeps Fortnite in the headlines. Older audiences might prefer PUBG or Warzone, but younger crowds argue that Fortnite is one of the best online games to play with friends. Just limit their V-Bucks spending.</p>
<p><strong>Platform:</strong> Battle Royale<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1, Switch, iOS, Android<br />
<strong>Player count:</strong> 100</p>
<p><a class="ch_custom" href="https://www.epicgames.com/fortnite/en-US/home" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374158" title="Best online games divinity original sin 2" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="divinity original sin 2" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374158" title="Best online games divinity original sin 2" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2.jpg" alt="divinity original sin 2" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-divinity-original-sin-2-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="30_Divinity:-original-sin-2">30. Divinity: Original Sin 2</h3>
<p>Inspired by the classics like Baldur’s Gate, Divinity: Original Sin 2 is a critically acclaimed, top-down, turn-based fantasy RPG that’s considered one of the Best games to play with friends by anyone who’s into the genre. Yes, this is a challenging game, but it does offer you the freedom to play and explore in any way you choose. The entire game can be played solo or in co-op, so a mate can be the voice of reason, suggesting a stealthy approach to situations instead of just pickpocketing every character or setting them all on fire &#8211; NPCs included.</p>
<p><strong>Genre:</strong> RPG<br />
<strong>Platforms:</strong> PC, PS4, XB1, Switch<br />
<strong>Player count:</strong> 1 &#8211; 2</p>
<p><a class="ch_custom" href="https://divinity.game/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374175" title="Best online games phasmophobia" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games phasmophobia" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374175" title="Best online games phasmophobia" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia.jpg" alt="Best online games phasmophobia" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-phasmophobia-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="31_Phasmophobia">31. Phasmophobia</h3>
<p>With paranormal activity on the rise, it’s up to you and three friends to wield an array of equipment to investigate a haunting, and boy! It’s a creepy one. Setup cameras, use night vision and lose your shit as you experience whispers, moving objects and jump scares. Combining elements of Blair Witch, The Ring and Paranormal Activity, there are few scarier experiences that you and your friends can face from in front of a PC.</p>
<p><strong>Genre:</strong> Horror<br />
<strong>Platform:</strong> PC<br />
<strong>Player count:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://store.steampowered.com/app/739630/Phasmophobia/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374177" title="Best online games portal 2" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games portal 2" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374177" title="Best online games portal 2" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2.jpg" alt="Best online games portal 2" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-portal-2-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_11-64ded10783e04) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_11-64ded10783e04">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_11-64ded10783e04']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_11-64ded10783e04'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_11', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_11-64ded10783e04'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_11-64ded10783e04');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_11-64ded10783e04:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_11-64ded10783e04:90px}}          </style>
</div>
</div>
<h3 id="32_Portal-2">32. Portal 2</h3>
<p>Portal 2 is the classic puzzler that blew everyone away for its humour, unique design and compelling story. But it’s the innovative co-op mode and editing tools that see it endure and make the list of best online games to play with friends. So, team up with a friend to solve the specially designed two-player test chambers set across a separate co-op campaign. Then, carry on the mayhem across player-created test chambers and the free PC mods, which offer an endless stream of puzzling potential.</p>
<p><strong>Genre:</strong> Puzzle<br />
<strong>Platform:</strong> PC<br />
<strong>Player count:</strong> 1 &#8211; 2</p>
<p><a class="ch_custom" href="https://store.steampowered.com/app/620/Portal_2/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374186" title="Best online games uno with friends" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="uno with friends" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374186" title="Best online games uno with friends" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends.jpg" alt="uno with friends" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-uno-with-friends-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="33_Uno-with-friends">33. Uno with Friends</h3>
<p>Uno is that timeless game that appeals to everyone despite age, skill and now location! Uno with Friends is a free to play digital version of the classic card game. Join online games with random players or create private rooms for you and your friends and family. Arguably the only differences between digital Uno and the real thing are that no one can cheat in the online version or spill drinks on the cards.</p>
<p><strong>Genre:</strong> Card, social<br />
<strong>Platform:</strong> PC<br />
<strong>Player count:</strong> 2 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.microsoft.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374168" title="Best online games league of legends" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games league of legends" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374168" title="Best online games league of legends" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends.jpg" alt="Best online games league of legends" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-league-of-legends-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="34_League-of-legends">34. League of Legends</h3>
<p>This team-based strategy game can be overwhelming at first. Although, experimenting with the 140+ champions and finding a lineup that works for you can be satisfying. The objective of League of Legends is to traverse a map eliminating monsters and ultimately destroying your opponents base. It may not sound like much depth, but when you combine the sheer quantity of so many characters with the risk vs reward gameplay, you&#8217;ll start to see why over 115 million people play each month and why League of Legends is all over esports tournaments.</p>
<p><strong>Genre:</strong> Strategy<br />
<strong>Platform:</strong> PC<br />
<strong>Team size:</strong> 1 &#8211; 5</p>
<p><a class="ch_custom" href="https://oce.leagueoflegends.com/en-au/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374153" title="Best online games cs go" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="cs go concept art" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374153" title="Best online games cs go" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go.jpg" alt="cs go concept art" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-cs-go-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_12-64ded10783e60) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_12-64ded10783e60">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_12-64ded10783e60']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_12-64ded10783e60'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_12', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_12-64ded10783e60'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_12-64ded10783e60');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_12-64ded10783e60:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_12-64ded10783e60:90px}}          </style>
</div>
</div>
<h3 id="35_Counter-strike:-global-offensive">35. Counter-Strike: Global Offensive</h3>
<p>Counter-Strike Global Offensive, or CS: GO, is the latest iteration of the team-based multiplayer experience pioneered by the franchise about 20 years ago. CS: GO updates the classic formula with refined gameplay but revives the classic operators, weapons, modes and locations from the original with new content to keep veterans engaged. Whether you’re forming a squad with mates to pass a night in or chasing that esports glory, Counter-Strike oozes potential.</p>
<p><strong>Genre:</strong> Team shooter<br />
<strong>Platform:</strong> PC<br />
<strong>Team size:</strong> 2 &#8211; 5</p>
<p><a class="ch_custom" href="https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374176" title="Best online games pokemon go" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games pokemon go" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374176" title="Best online games pokemon go" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go.jpg" alt="Best online games pokemon go" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pokemon-go-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="36_Pokémon-go">36. Pokémon Go</h3>
<p>The social phenomenon from a few years back continues thanks to a steady stream of new content that works to make Pokémon Go one of the best online games to play with friends. Catch wild Pokemon out in the community, train them, then battle friends or randoms to chase that dream of leaving your life behind and becoming a certified Pokémon trainer.</p>
<p><strong>Genre:</strong> Social<br />
<strong>Platforms:</strong> iOS, Android<br />
<strong>Friends list:</strong> 1 &#8211; 400</p>
<p><a class="ch_custom" href="https://pokemongolive.com/en/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374178" title="Best online games pubg" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="pubg or playerunknown's battlegrounds" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374178" title="Best online games pubg" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg.jpg" alt="pubg or playerunknown's battlegrounds" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-pubg-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="37_Playerunknown's-battlegrounds">37. PlayerUnknown&#8217;s Battlegrounds</h3>
<p>PUBG or PlayrerUnknown’s Battlegrounds is arguably the original battle royale. Now, you’ve heard this before. 100 players skydive onto an island and battle it out until one player or squad is left standing. So Fortnite, Warzone and Apex Legends all stole the formula from PUBG and twisted it in their unique ways. But PUBG works, not just because it’s the OG. But because it has tight gunplay, tense action and less flossing. It’s a slightly more realistic approach to this popular competitive genre for you and some friends to squad up and take on the ever-expanding lineup of maps and modes.</p>
<p><strong>Genre:</strong> Battle Royale<br />
<strong>Platforms:</strong> PC, PS4, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://na.battlegrounds.pubg.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-356589" title="Fallout 76 screenshot 5" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Fallout 76 screenshot 5" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-356589" title="Fallout 76 screenshot 5" src="https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5.jpg" alt="Fallout 76 screenshot 5" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/04/fallout-76-screenshot-5-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_13-64ded10783ebc) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_13-64ded10783ebc">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_13-64ded10783ebc']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_13-64ded10783ebc'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_13', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_13-64ded10783ebc'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_13-64ded10783ebc');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_13-64ded10783ebc:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_13-64ded10783ebc:90px}}          </style>
</div>
</div>
<h3 id="38_Fallout-76">38. Fallout 76</h3>
<p>Over the past few years, Fallout 76 has transformed from a joke to become a solid RPG and a decent way to pass the time with some mates. Is Fallout 76 one of the best online games? That’s questionable. But is it enjoyable, and the gameplay is quintessentially Fallout. The addition of friends adds new layers to the formula, and fans of the franchise will find a lot to like within this post-apocalyptic Appalachia.</p>
<p><strong>Genre:</strong> MMORPG<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://fallout.bethesda.net/en/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374180" title="Best online games risk of rain 2" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="risk of rain 2 cover art" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374180" title="Best online games risk of rain 2" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2.jpg" alt="risk of rain 2 cover art" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-risk-of-rain-2-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="39_Risk-of-rain-2">39. Risk of Rain 2</h3>
<p>This cartoony co-op rogue-like sees you and your friends team up to fight through chaotic alien hordes in an attempt to escape a hostile planet. Each playable character class offers unique ways to play, but at its core, Risk of Rain 2 is all about the action-packed gauntlets and larger than life bosses. If you’re looking for some gun-blazing action to fill a few hours and don’t mind a laugh or two, you can’t go wrong with this acclaimed shooter.</p>
<p><strong>Genre:</strong> Rogue-like<br />
<strong>Platforms:</strong> PC, PS4, XB1, Switch<br />
<strong>Squad size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.riskofrain.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374157" title="Best online games diablo 3" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="diablo 3 necromancer art" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374157" title="Best online games diablo 3" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3.jpg" alt="diablo 3 necromancer art" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-diablo-3-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="40_Diablo-iii">40. Diablo III</h3>
<p>This popular hack n slash looter launched almost a decade ago. Diablo 4 is even on the schedule. And yet, there are plenty of reasons to continue playing Diablo 3 or pick it up for the first time. You choose a character class, slay hordes and hordes and hordes of demons, and keep grinding for that epic loot. It’s a simple yet satisfying design with over 20 seasons worth of content that does not appear to be slowing down anytime soon.</p>
<p><strong>Genre:</strong> Action RPG<br />
<strong>Platforms:</strong> PC, PS4, XB1, Switch<br />
<strong>Player count:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://us.diablo3.com/en-us/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374185" title="Best online games tetris 99" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games tetris 99" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374185" title="Best online games tetris 99" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99.jpg" alt="Best online games tetris 99" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-tetris-99-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_14-64ded10783f8c) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_14-64ded10783f8c">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_14-64ded10783f8c']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_14-64ded10783f8c'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_14', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_14-64ded10783f8c'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_14-64ded10783f8c');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_14-64ded10783f8c:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_14-64ded10783f8c:90px}}          </style>
</div>
</div>
<h3 id="41_Tetris-99">41. Tetris 99</h3>
<p>It’s hard to believe that falling block puzzles could work as a battle royale, but Tetris 99 successfully turns the classic game into modern competitive mayhem. Tetris 99 sees you and 98 other players all complete separate puzzles at the same time. Every time you clear two rows, a random player is hit with garbage blocks, limiting their possible moves. It keeps going like this until one player remains. You can play Tetris 99 free with an active Nintendo Switch Online subscription.</p>
<p><strong>Genre:</strong> Battle Royale, puzzle<br />
<strong>Platform:</strong> Switch<br />
<strong>Player count:</strong> 99</p>
<p><a class="ch_custom" href="https://www.nintendo.com/games/detail/tetris-99-switch/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-377065" title="Best online games houseparty" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games houseparty" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-377065" title="Best online games houseparty" src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty.jpg" alt="Best online games houseparty" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-houseparty-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="42_Houseparty">42. Houseparty</h3>
<p>Don’t confuse Houseparty with the sleazy PC game of the same name. We’re talking about the dedicated mobile app that’s designed specifically for socialising from a distance. So yeah, it’s another video chat app. But what makes Houseparty the go-to is its integrated games. You can play Uno, drawing games and even stream Fortnite to your friends. If Mum and Dad have Android phones, but the siblings use Apple, meet in the middle by downloading Houseparty for free.</p>
<p><strong>Genre:</strong> Social<br />
<strong>Platforms:</strong> iOS, Android<br />
<strong>Group chat:</strong> 2 &#8211; 10</p>
<p><a class="ch_custom" href="https://houseparty.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-377059" title="Best online games rainbow six" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games rainbow six" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-377059" title="Best online games rainbow six" src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six.jpg" alt="Best online games rainbow six" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-rainbow-six-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="43_Rainbow-six-siege">43. Rainbow Six Siege</h3>
<p>For a while now, <a title="Michael B. Jordan to Star in ‘Rainbow Six’ Movie from ‘John Wick’ Director" href="https://manofmany.com/entertainment/movies-tv/michael-b-jordan-rainbow-six">Rainbow Six</a> Siege has been considered one of the best online multiplayer games thanks to its rewarding tactical gameplay and continually expanding roster of operators and maps. The simple objectives become tense standoffs as players tear through walls, drop drones and work together in tight formation. There’s a steep learning curve to this one, so make sure your squad stays in communication throughout each round.</p>
<p><strong>Genre:</strong> Tactical shooter<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Squad size:</strong> 5</p>
<p><a class="ch_custom" href="https://www.ubisoft.com/en-au/game/rainbow-six/siege" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374191" title="Best online games halo" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="halo the master chief collection" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374191" title="Best online games halo" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo.jpg" alt="halo the master chief collection" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-halo-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_15-64ded10783ff3) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_15-64ded10783ff3">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_15-64ded10783ff3']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_15-64ded10783ff3'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_15', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_15-64ded10783ff3'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_15-64ded10783ff3');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_15-64ded10783ff3:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_15-64ded10783ff3:90px}}          </style>
</div>
</div>
<h3 id="44_Halo:-the-master-chief-collection">44. Halo: The Master Chief Collection</h3>
<p>The only thing better than playing Halo with friends is playing ALL the Halos with friends. The Master Chief Collection features six Halo games – each build for co-op play – now collected in a neat little package and enhanced with 4K and HDR where available. There’s also a dedicated multiplayer component for those looking for a more competitive experience. The Halo collection, along with Sea of Thieves and Forza Horizon 4 are all part of Xbox Game Pass, making that subscription service a great way to start exploring this list.</p>
<p><strong>Genre:</strong> First-person shooter<br />
<strong>Platforms:</strong> PC, XBX/S, XB1<br />
<strong>Squad size:</strong> Varies between modes/games</p>
<p><a class="ch_custom" href="https://www.xbox.com/en-AU/games/halo-the-master-chief-collection" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-374155" title="Best online games decurse" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="decurse" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-374155" title="Best online games decurse" src="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse.jpg" alt="decurse" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse.jpg 1200w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2020/01/best-online-games-decurse-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="45_Decurse">45. Decurse</h3>
<p>Not everyone is into racing, shooting and looting. That’s where Decurse comes in. Decurse is a cutesy farming sim where you build a magical kingdom at the bottom of the ocean. You grow, build, trade and sell on your quest to remove a curse and successfully kill time between real-life activities &#8211; like with all good mobile games. Connect with your friends online to compete in races, land on leaderboards and trade to beat that free to play grind.</p>
<p><strong>Genre:</strong> Farming, sim<br />
<strong>Platforms:</strong> iOS, Android<br />
<strong>Player count:</strong> 1+</p>
<p><a class="ch_custom" href="https://www.bigfishgames.com/game/decurse/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-377062" title="Best online games moving out" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="moving out party game" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-377062" title="Best online games moving out" src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out.jpg" alt="moving out party game" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-moving-out-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="46_Moving-out">46. Moving Out</h3>
<p>Getting roped into moving furniture is a sure-fire way to ruin a weekend, yet this indie game turns the world’s worst job into the ideal way to spend a few hours indoors. Racing against the clock, you and the other players work together to gather up boxes, white goods, awkward-shaped furniture and more, then load it in the removal truck with bronze, silver and gold medals awarded for performance. Anyone familiar with Overcooked will feel right at home here. Moving Out is ideal for keeping entire families entertained during the wet weather or another lockdown.</p>
<p><strong>Genre:</strong> Party<br />
<strong>Platforms:</strong> PC, PS4, XB1, Switch<br />
<strong>Player count:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.team17.com/games/moving-out/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-377064" title="Best online games gears 5" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games gears 5" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-377064" title="Best online games gears 5" src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5.jpg" alt="Best online games gears 5" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-gears-5-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_16-64ded10784050) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_16-64ded10784050">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_16-64ded10784050']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_16-64ded10784050'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_16', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_16-64ded10784050'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_16-64ded10784050');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_16-64ded10784050:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_16-64ded10784050:90px}}          </style>
</div>
</div>
<h3 id="47_Gears-5">47. Gears 5</h3>
<p>The Gears of War franchise has always championed co-op play and features stacks of varied multiplayer modes. The latest entry in the series, Gears 5, is no exception. First, the story campaign features hours of three-player action online or via split-screen, making it one of the best online games on the market. Afterwards, check out Escape: A new, aggressive, high-stakes mode featuring a three-player suicide squad working together to take out enemy hives from within. Then Horde and Versus modes keep you playing with more teamwork or competitive play. Gears 5 is a huge package that will keep you busy for the foreseeable future.</p>
<p><strong>Genre:</strong> Team shooter<br />
<strong>Platforms:</strong> PC, XBX/S, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 3</p>
<p><a class="ch_custom" href="https://www.gears5.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-377066" title="Best online games borderlands 3" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="borderlands 3" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-377066" title="Best online games borderlands 3" src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3.jpg" alt="borderlands 3" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-borderlands-3-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="48_Borderlands-3">48. Borderlands 3</h3>
<p>Borderlands 3 is a co-op game that features cel-shaded first-person shooter action where you take on insane enemies, score loads of loot and save your home from the most ruthless cult leaders in the galaxy. Players tear through hostile deserts, battle across war-torn cityscapes, navigate deadly bayous, and more. The lengthy campaign and unique characters will keep everyone occupied for dozens of hours.</p>
<p><strong>Genre:</strong> First-person shooter<br />
<strong>Platforms:</strong> PC, PS5, PS4, XBX/S, XB1<br />
<strong>Squad size:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://borderlands.com/en-US/" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-377061" title="Best online games world of warcraft classic" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="world of warcraft classic" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-377061" title="Best online games world of warcraft classic" src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5.jpg" alt="world of warcraft classic" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-far-cry-5-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p>
<h3 id="49_World-of-warcraft-classic">49. World of Warcraft Classic</h3>
<p>Jumping back to the early days of this online sensation, World of Warcraft Classic allows players to return to the popular game in its original state. Meaning familiar, fun gameplay without hefty updates and unwanted changes. This option had been requested for a long time, and players finally got their wish in late 2019. So if you played WOW back in 2006 or always thought about giving it a go, this new Classic version is the best place to start.</p>
<p><strong>Genre:</strong> MMORPG<br />
<strong>Platforms:</strong> PC<br />
<strong>Party size:</strong> 1 &#8211; 5</p>
<p><a class="ch_custom" href="https://us.shop.battle.net/en-us/family/world-of-warcraft-classic" target="_blank" rel="noopener">Check it out</a></p>
<p><img decoding="async" class="alignnone size-full wp-image-377058" title="Best online games deep rock galactic" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20800'%3E%3C/svg%3E" alt="Best online games deep rock galactic" width="1200" height="800" data-lazy-srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic-600x400.jpg 600w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic.jpg" /><noscript><img decoding="async" class="alignnone size-full wp-image-377058" title="Best online games deep rock galactic" src="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic.jpg" alt="Best online games deep rock galactic" width="1200" height="800" srcset="https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic.jpg 1200w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic-400x267.jpg 400w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic-280x187.jpg 280w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic-768x512.jpg 768w, https://manofmany.com/wp-content/uploads/2021/07/best-online-games-deep-rock-galactic-600x400.jpg 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></p> <div class="mom-ads__wrapper"> <div class="mom-ads__inner mom-ads__inner--labeled mom-ads__inner--labeled--top" style="min-height:calc(var(--gam-wrapper__22715092907-manofmany-article_1-incontent_17-64ded107840ab) + 25px)">
<div id="gam-wrapper__22715092907-manofmany-article_1-incontent_17-64ded107840ab">
<script type="text/javascript">
        googletag.cmd.push(function() {
          window.MomApp = window.MomApp || {};

                    if ('undefined' !== typeof window.MomApp.prefetchSlots?.['gam-wrapper__22715092907-manofmany-article_1-incontent_17-64ded107840ab']) {
                        window.MomApp.prefetchSlots['gam-wrapper__22715092907-manofmany-article_1-incontent_17-64ded107840ab'].setTargeting(
              'scroll', 1            );
                      } else {
                        googletag.defineSlot(
              '/22715092907/ManOfMany/article_1/incontent_17', [300,250], 'gam-wrapper__22715092907-manofmany-article_1-incontent_17-64ded107840ab'
            ).defineSizeMapping(
              gamData.sizeMap['incontent']
            ).setTargeting(
              'refresh', 'false'
            ).addService(
              googletag.pubads()
            ).setTargeting(
              'scroll', 1            );
          }

          googletag.display('gam-wrapper__22715092907-manofmany-article_1-incontent_17-64ded107840ab');
        });
      </script>
</div>
<style>
            @media screen and (min-width:0px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_17-64ded107840ab:300px}}            @media screen and (min-width:1200px){.mom-ads__inner{--gam-wrapper__22715092907-manofmany-article_1-incontent_17-64ded107840ab:90px}}          </style>
</div>
</div>
<h3 id="50_Deep-rock-galactic">50. Deep Rock Galactic</h3>
<p>Part Minecraft, part Borderlands, complete original, Deep Rock Galactic is a co-op shooter for up to four players. You take on the roles of badass space dwarves who blast through procedurally generated caves taking on endless hordes of alien monsters. Every landscape is fully destructible, making each playthrough unique, and the class-based dwarves cater to everyone’s playstyles.</p>
<p><strong>Genre:</strong> First-person shooter<br />
<strong>Platforms:</strong> PC, XBX/S, XB1<br />
<strong>Player count:</strong> 1 &#8211; 4</p>
<p><a class="ch_custom" href="https://www.deeprockgalactic.com/" target="_blank" rel="noopener">Check it out</a></p>
<h3 id="51_valheim">51. valheim</h3>
<p>valheim is a brutal survival game and one of the best games to play online. Set in Viking purgatory, up to 10 players battle, build and conquer together to please Odin and bring order to the afterlife. valheim is still in early access, and yet, it has already sold over 5 million copies. So, there’s no shortage of players and plenty of benefits for those who want to get in early.</p>
<p><strong>Genre:</strong> Survival<br />
<strong>Platform:</strong> PC<br />
<strong>Player count:</strong> 1 &#8211; 10</p>
<p><a class="ch_custom" href="https://www.valheimgame.com/" target="_blank" rel="noopener">Check it out</a></p>
<p><strong>You&#8217;ll also like:</strong><br />
<a href="https://manofmany.com/entertainment/movies-tv/scariest-horror-movies-according-to-science">20 Scariest Horror Movies of All Time According to Science</a><br />
<a href="https://manofmany.com/entertainment/gaming/where-to-buy-ps5-australia">Where to Buy a PS5 in Australia: 10 Restock Spots</a><br />
<a href="https://manofmany.com/entertainment/gaming/best-e3-games-2021">10 Best New Games Revealed at E3 2021</a></p>
<h3 id="general-faq">General FAQ</h3>
<div class="entry-meta f-entry-meta">
"""
for s in games_raw.splitlines():
    if "h3" in s:
        print(s.split('"')[1])

print("#################################################################")
less_raw = """
1_Destiny-2
2_Call-of-duty:-warzone
3_Among-us
4_Sea-of-thieves
5_Nba-2k20
6_Overcooked:-all-you-can-eat
7_Minecraft
8_Super-smash-bros-ultimate
9_Gta-online
10_Path-of-exile
11_Final-fantasy-xiv:-a-realm-reborn
12_Rocket-league
13_Draw-something
14_Fall-guys:-ultimate-knockout
15_Dead-by-daylight
16_Words-with-friends-2
17_Forza-horizon-4
18_Apex-legends
19_Animal-crossing:-new-horizons
20_Warframe
21_Phantom-abyss
22_Red-dead-online
23_Mario-kart-8-deluxe
24_Crash-team-racing:-nitro-fuel
25_The-elder-scrolls-online
26_Spellbreak
-27_Mnster-hunter-world
28_Golf-battle
29_Fortnite
30_Divinity:-original-sin-2
31_Phasmophobia
32_Portal-2
33_Uno-with-friends
34_League-of-legends
35_Counter-strike:-global-offensive
36_Pokémon-go
37_Playerunknown's-battlegrounds
38_Fallout-76
39_Risk-of-rain-2
40_Diablo-iii
41_Tetris-99
42_Houseparty
43_Rainbow-six-siege
44_Halo:-the-master-chief-collection
45_Decurse
46_Moving-out
47_Gears-5
48_Borderlands-3
49_World-of-warcraft-classic
50_Deep-rock-galactic
51_valheim
"""

end: list[str] = [s.split("_")[1].replace("-", " ").title() for s in less_raw.splitlines() if s]
print(end)

mc = mouse.Controller()
ml = mouse.Listener()
kc = keyboard.Controller()

time.sleep(5)
for s in ["test", *end]:
    mc.position = (1189, 123)
    time.sleep(0.3)
    mc.click(mouse.Button.left, 1)
    for _ in range(4):
        time.sleep(0.5)
        kc.tap(keyboard.Key.tab)
    time.sleep(0.3)
    kc.type(f"Jeux - {s}")
    print(s)
    time.sleep(0.3)
    mc.position = (1468, 440)
    time.sleep(0.3)
    mc.click(mouse.Button.left, 1)
    time.sleep(0.3)
    mc.position = (1665, 951)
    time.sleep(0.3)
    mc.click(mouse.Button.left, 1)
    time.sleep(0.3)
print("#################################################################")


# print current mouse position
print(mc.position)
