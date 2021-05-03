import os
import re
import urllib.request
import xml.dom.minidom
import xml.etree.ElementTree as ET

# source links:
# https://support.appsflyer.com/hc/en-us/articles/360012640377-Apple-SKAdNetwork-IDs-for-advertisers-who-use-ads#:~:text=At%20a%20glance%3A%20AppsFlyer%20ad,to%20populate%20the%20app%20info.
# https://developers.ironsrc.com/ironsource-mobile/unity/ios-14-network-support/
# https://developers.mopub.com/publishers/skadnetwork-ids-manager/
# https://unityads.unity3d.com/help/ios/skadnetwork-ids

def start_fetch():
    encoding = 'utf-8'
    # Unity List
    contents = urllib.request.urlopen("https://skan.mz.unity3d.com/v2/partner/skadnetworks.plist.xml?_ga=2.179301732.1188576647.1611804828-880817938.1611804828").read()
    contents = str(contents, encoding)
    # print(contents)
    result1 = re.findall("[a-z|0-9]{10}\.skadnetwork", contents)
    # print(result1)
    print("Unity List: " + str(len(result1)))

    contents = urllib.request.urlopen("https://us-central1-mopub-mediation.cloudfunctions.net/getSKAdNetworkIds/%22all%22").read()
    contents = str(contents, encoding)
    result2 = re.findall("[a-z|0-9]{10}\.skadnetwork", contents)
    print("mopub List: " + str(len(result2)))

    contents = urllib.request.urlopen("https://developers.ironsrc.com/ironsource-mobile/unity/ios-14-network-support/").read()
    contents = str(contents, encoding)
    result3 = re.findall("[a-z|0-9]{10}\.skadnetwork", contents)
    print("ironsource List: " + str(len(result3)))

    contents = urllib.request.urlopen("https://docs.google.com/spreadsheets/d/e/2PACX-1vSqwIBW3FzbrXKqluDQ2hEec7zcvVrxQ02ivWsHnGQTvLMeFmHHjGz1R5TVy6_cqAIVh0pAy4Yud7Qx/pub?gid=0&single=true&output=csv").read()
    contents = str(contents, encoding)
    result4 = re.findall("[a-z|0-9]{10}\.skadnetwork", contents)
    print("appsflyer List: " + str(len(result4)))

    contents = urllib.request.urlopen("https://www.skanids.com/").read()
    contents = str(contents, encoding)
    result5 = re.findall("[a-z|0-9]{10}\.skadnetwork", contents)
    print("skanids.com List: " + str(len(result5)))

    # mobpub dumb enough not to add their ids in the list they provided
    mobpubList = ["cdkw7geqsh.skadnetwork", "qyjfv329m4.skadnetwork"]

    resultlist = list(set(result1 + result2 + result3 + result4 + result5 + mobpubList))

    print("Total List: " + str(len(resultlist)))

    #create XML
    xmlarray = ET.Element('array')
    for x in resultlist:
        dict = ET.SubElement(xmlarray, 'dict')
        keyelement = ET.SubElement(dict, 'key')
        keyelement.text = "SKAdNetworkIdentifier"
        strelement = ET.SubElement(dict, 'string')
        strelement.text = x

    # ET.dump(xmlarray)


    # mydata = ET.tostring(xmlarray)
    # myfile = open("SkAdNetworkId.xml", "w")
    # myfile.write(str(mydata,encoding))

    xml_string = xml.dom.minidom.parseString(ET.tostring(xmlarray)).toprettyxml()
    xml_string = os.linesep.join([s for s in xml_string.splitlines() if s.strip()])  # remove the weird newline issue
    with open("SkAdNetworkIds.xml", "w") as file_out:
        file_out.write(xml_string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_fetch()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
