# End-to-End-MLOPS-Project-with-ETL-Pipeline-Network-Security-System

This project aims to create a robust pipeline for detecting phishing websites using machine learning. It covers essential aspects of MLOps, such as data ingestion, validation, transformation, model training, deployment, and continuous integration/continuous deployment (CI/CD).
# Feature Explanations
1. having_IP_Address:

Whether the URL contains an IP address instead of a domain name.
Phishing URLs often use IP addresses.
1: No IP address, legitimate.
0: Neutral.
-1: Contains an IP address, phishing.
URL_Length:

Checks the length of the URL. Longer URLs can indicate phishing.
1: Short, legitimate.
0: Medium-length.
-1: Long, phishing.
Shortining_Service:

Whether the URL uses a shortening service like bit.ly.
1: Not shortened, legitimate.
-1: Shortened, phishing.
having_At_Symbol:

Checks if the URL contains an "@" symbol, which can redirect users to another URL.
1: No "@" symbol, legitimate.
-1: Contains "@", phishing.
double_slash_redirecting:

Whether there is a "//" redirect after the domain in the URL.
1: No redirect, legitimate.
-1: Redirect present, phishing.
Prefix_Suffix:

Checks if the domain has a hyphen ("-"), often used in phishing URLs.
1: No hyphen, legitimate.
-1: Hyphen present, phishing.
having_Sub_Domain:

The number of subdomains in the URL. More subdomains can indicate phishing.
1: Few subdomains, legitimate.
0: Moderate number of subdomains.
-1: Many subdomains, phishing.
SSLfinal_State:

Checks the SSL/TLS certificate status of the website.
1: Valid SSL, legitimate.
0: Suspicious or self-signed SSL.
-1: No SSL, phishing.
Domain_registeration_length:

Length of the domain's registration period. Shorter registrations often indicate phishing.
1: Long registration, legitimate.
-1: Short registration, phishing.
Favicon:

Checks the source of the favicon (website icon). Phishing sites may use unrelated favicons.
1: Favicon matches domain, legitimate.
-1: Favicon from a different domain, phishing.
port:

Whether unusual ports (other than 80 or 443) are open.
1: No unusual ports, legitimate.
-1: Unusual ports, phishing.
HTTPS_token:

Checks if "HTTPS" is present in the domain name, which may falsely imply security.
1: No HTTPS token in domain, legitimate.
-1: HTTPS token in domain, phishing.
Request_URL:

Percentage of external objects (like images) loaded from other domains.
1: Low percentage, legitimate.
0: Moderate percentage.
-1: High percentage, phishing.
URL_of_Anchor:

Percentage of anchor tags with empty or external links.
1: Low percentage, legitimate.
0: Moderate percentage.
-1: High percentage, phishing.
Links_in_tags:

Percentage of links in , <script>, or tags.
1: Low percentage, legitimate.
0: Moderate percentage.
-1: High percentage, phishing.
SFH (Server Form Handler):

Checks the action attribute of form tags to see if it’s empty or points to a different domain.
1: Legitimate action.
0: Suspicious.
-1: Phishing.
Submitting_to_email:

Checks if forms on the website directly send data to email addresses.
1: No, legitimate.
-1: Yes, phishing.
Abnormal_URL:

Whether the URL structure matches typical patterns for the domain.
1: Normal structure, legitimate.
-1: Abnormal structure, phishing.
Redirect:

Number of redirections the URL performs.
1: Few or none, legitimate.
-1: Many redirects, phishing.
on_mouseover:

Checks for changes in status bar content when hovering over elements.
1: No changes, legitimate.
-1: Changes present, phishing.
RightClick:

Whether right-click functionality is disabled on the website.
1: Not disabled, legitimate.
-1: Disabled, phishing.
popUpWidnow:

Checks for pop-up windows triggered by the website.
1: No pop-ups, legitimate.
-1: Pop-ups present, phishing.
Iframe:

Checks for the presence of hidden iframes.
1: No hidden iframes, legitimate.
-1: Hidden iframes present, phishing.
age_of_domain:

Age of the domain in months. Older domains are usually more trustworthy.
1: Old, legitimate.
-1: New, phishing.
DNSRecord:

Checks if DNS records exist for the domain.
1: Records exist, legitimate.
-1: No records, phishing.
web_traffic:

Traffic rank of the website. Lower rank indicates more traffic.
1: High traffic, legitimate.
0: Moderate traffic.
-1: Low traffic, phishing.
Page_Rank:

Google PageRank score of the website.
1: High PageRank, legitimate.
-1: Low PageRank, phishing.
Google_Index:

Checks if the website is indexed by Google.
1: Indexed, legitimate.
-1: Not indexed, phishing.
Links_pointing_to_page:

Number of backlinks pointing to the website.
1: Many links, legitimate.
0: Moderate number of links.
-1: Few links, phishing.
Statistical_report:

Checks if the website is flagged by statistical or threat analysis tools.
1: Not flagged, legitimate.
-1: Flagged, phishing.
Result:

The target variable indicating whether the URL is phishing.
1: Legitimate.
-1: Phishing.
