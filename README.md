# NekoPy
![neko](https://user-images.githubusercontent.com/76231670/120505256-b7cf0d80-c3bc-11eb-8227-d8afe0cefbd4.jpg)

NekoPy is a simple CLI tool developed in Python.

Made under Pycharm Community IDE.

The intention is (in a closer future) make a scalable CLI tool to integrate Python with a myriad of different API and Applications.

Until now, it does:

#echo

#check the weather via OpenWeather API.

#Requirements
----------
<ul>
  <li>Python 3.9 </li>
  <li>Pip 21.1.2</li>
  <li>Click 7.1.2 or latest</li>
  <li>PyOWM 3.2.0 or latest</li>
</ul>
<p> You will also need to register into <a href="https://openweathermap.org/">OpenWeatherMap</a> and obtain a token:
<ul>
  <li>API Key Token</li>
</ul>

#Installation
----------
<ol>
  <li> Clone this Repository</li>
  <li> Create a file named <code>config.py</code> contained the information as follows:</li>

<div class="highlight highlight-html-py position-relative">
  </br>
  <pre>
    # WX Config
    
    WX_API_KEY = 'YOUR_API_KEY_TOKEN'
    WX_LOCATION = 'YOUR_LOCATION'
    WX_METRIC_TEMP = 'CELSIUS_OR_FAHRENHEIT'
    WX_METRIC_WIND = 'MILES_OR_KILOMETERS_HOUR'
  </pre>
  <div class="zeroclipboard-container position-absolute right-0 top-0">
   <clipboard-copy class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" aria-label="Copy" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# WX Config WX_API_KEY = 'YOUR_API_KEY_TOKEN' WX_LOCATION = 'YOUR_LOCATION' WX_METRIC_TEMP = 'CELSIUS_OR_FAHRENHEIT' WX_METRIC_WIND = 'MILES_OR_KILOMETERS_HOUR' " tabindex="0" role="button">
   </cipboard-copy>
  </div>
</div>
  <li> Do not forget to put your credentials and the data you want to track!</li>
 </ol>
     
#Image Attribution:
---------
  <p> Neko Cat: Free license via <a href="https://pexels.com/">Pexels</a>.<p>
