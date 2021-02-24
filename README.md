# Fetching all available SkAdNetworkIds
iOS 14 requires `Source App` to include a list of different platforms Ids of SkAdNetwork in order to<br>
track Ads attribution properly.

This is a simple python script that fetches SkAdNetworkIds from different sources<br>
and combine as a xml with most platforms Ids and can be used in iOS info.plist file.

Script can run without any python library dependency.
Use python 3 to run the script.

The generated XML as follow


    <?xml version="1.0" ?>
    <array>
      <dict>
        <key>SKAdNetworkIdentifier</key>
        <string>nu4557a4je.skadnetwork</string>
      </dict>
      ....
    </array>

**Remember** to add `<key>SKAdNetworkItems</key>` in info.plist as the key name.


Source list:

https://support.appsflyer.com/hc/en-us/articles/360012640377-Apple-SKAdNetwork-IDs-for-advertisers-who-use-ads#:~:text=At%20a%20glance%3A%20AppsFlyer%20ad,to%20populate%20the%20app%20info.

https://developers.ironsrc.com/ironsource-mobile/unity/ios-14-network-support/

https://developers.mopub.com/publishers/skadnetwork-ids-manager/

https://unityads.unity3d.com/help/ios/skadnetwork-ids
