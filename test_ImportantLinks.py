import pytest
from unittest.mock import patch
import io
from important import *
from generalLinks import aboutUs
import os, sys

current_script_directory = os.path.dirname(os.path.abspath(__file__))

parent_directory = os.path.join(current_script_directory, '..')
sys.path.append(parent_directory)

# Mock the input function to provide user input for your functions
def mock_input(mock_values):
    return lambda _: mock_values.pop(0)

# Mock the print function to capture printed output
def mock_print(captured_output):
    def printer(s):
        captured_output.append(s)

    return printer

# Test copyrightNotice function
def test_copyright_notice(capsys):
    with patch('builtins.input', side_effect=['1']):
        copyrightNotice()
        captured = capsys.readouterr()
        assert "Copyright © 2023 TeamAlaska. All rights reserved." in captured.out

def test_about_us(capsys):
    with patch('builtins.input', side_effect=['2']):
        aboutUs()
        captured = capsys.readouterr()
        aboutUsText = 'inCollege: Welcome to inCollege, the world\'s largest college student network with many users in many countries and territories worldwide.'
        wrappedText = textwrap.fill(aboutUsText, width=80)
        print("")
        assert wrappedText in captured.out

def test_accessibility(capsys):
    with patch('builtins.input', side_effect=['3']):
        accessibility()
        captured = capsys.readouterr()
        accText = 'At inCollege, we\'re committed to accessibility. We believe in making our applications and services accessible to all users, regardless of ability. Our goal is to provide an inclusive experience by implementing features that support individuals with diverse needs and disabilities. We continuously work to enhance our accessibility and adhere to many of the available standards and guidelines. If you encounter any issues or have suggestions for improvement, please contact us.'
        wrappedText = textwrap.fill(accText, width=80)
        print("")
        assert wrappedText in captured.out

def test_user_agreement(capsys):
    with patch('builtins.input', side_effect=['4']):
        userAgreement()
        captured = capsys.readouterr()
        uaText = 'By using the services provided by inCollege, you agree to be bound by the terms and conditions outlined herein. These terms are designed to ensure a safe, secure, and respectful use of our platform for all users. Users must not exploit, misuse, or engage in activities that violate any applicable laws or regulations while using our services. inCollege reserves the right to modify these terms at any time, with changes effective immediately upon posting to our site. Your continued use of our services following any modifications signifies your acceptance of the updated terms. For any queries or concerns regarding this agreement, please contact us.'
        wrappedText = textwrap.fill(uaText, width=80)
        print("")
        assert wrappedText in captured.out

def test_privacy_policy(capsys):
    with patch('builtins.input', side_effect=['5']):
        privacyPolicy()
        captured = capsys.readouterr()
        ppText = 'inCollege values your privacy. We are committed to safeguarding the privacy of our website visitors and service users. Our policy outlines the type of personal information we collect, how we use it, and the measures we take to secure it. We only collect information necessary for delivering our services and enhancing user experience. Under no circumstances will your data be sold or shared with unauthorized third parties without your consent. Please be aware that our privacy practices may be amended over time as we adapt to new regulatory requirements. For detailed information and updates, kindly contact us.'
        wrappedText = textwrap.fill(ppText, width=80)
        print("")
        assert wrappedText in captured.out

def test_cookie_policy(capsys):
    with patch('builtins.input', side_effect=['6']):
        cookiePolicy()
        captured = capsys.readouterr()
        cpText = 'inCollege uses cookies to enhance your experience while navigating through our website. Cookies are small data files placed on your device that allow us to collect information on how you interact with our services, enabling us to optimize functionality, improve performance, and tailor content to your preferences. By using our site, you consent to the use of cookies in accordance with this policy. For more information on the types and purposes of cookies we use, or to adjust your cookie preferences, please contact us.'
        wrappedText = textwrap.fill(cpText, width=80)
        print("")
        assert wrappedText in captured.out

def test_copyright_policy(capsys):
    with patch('builtins.input', side_effect=['7']):
        copyrightPolicy()
        captured = capsys.readouterr()
        crpText = 'All content, including text, graphics, logos, images, and software, appearing on inCollege\'s website is the exclusive property of inCollege or its content suppliers and is protected by international copyright laws. Unauthorized use, reproduction, or distribution of this content without the express written consent of inCollege is strictly prohibited. For inquiries about obtaining permission to use any content on our site or for any copyright-related questions, please contact us.'
        wrappedText = textwrap.fill(crpText, width=80)
        print("")
        assert wrappedText in captured.out

def test_brand_policy(capsys):
    with patch('builtins.input', side_effect=['8']):
        brandPolicy()
        captured = capsys.readouterr()
        bpText = 'inCollege\'s logos, trademarks, icons, and other intellectual property (“Brand Assets”) are valuable assets that represent our company and products. These Brand Assets should be used in a manner that is consistent with our brand identity, values, and legal guidelines. Unauthorized use, modification, or manipulation of any of inCollege\'s Brand Assets is strictly prohibited. Users and partners wishing to use or refer to inCollege\'s Brand Assets for any public or commercial purpose must obtain written approval from inCollege beforehand. For more information, guidelines, or requests related to our Brand Policy, please contact us.'
        wrappedText = textwrap.fill(bpText, width=80)
        print("")
        assert wrappedText in captured.out


if __name__ == '__main__':
    pytest.main()

