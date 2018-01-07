from pritunl.settings.group_mongo import SettingsGroupMongo

class SettingsApp(SettingsGroupMongo):
    group = 'app'
    fields = {
        'secondary_mongodb_uri': None,
        'redis_uri': None,
        'redis_timeout': 6,
        'server_debug': False,
        'server_ssl': True,
        'server_port': 443,
        'server_internal_port': 9756,
        'server_auto_restart': True,
        'reverse_proxy': False,
        'reverse_proxy_header': 'X-Forwarded-For',
        'redirect_server': True,
        'check_requests': True,
        'demo_mode': False,
        'allow_insecure_session': False,
        'auditing': None,
        'monitoring': None,
        'plugin_requred': None,
        'plugin_directory': '/var/lib/pritunl/plugins',
        'plugin_queue_size': 512,
        'plugin_queue_threads': 10,
        'influxdb_uri': None,
        'influxdb_prefix': 'pritunl_',
        'influxdb_interval': 3,
        'prometheus_port': 9780,
        'datadog_api_key': None,
        'settings_check_interval': 60,
        'key_link_timeout': 86400,
        'password_len_limit': 128,
        'public_ip_server': 'https://app.pritunl.com/ip',
        'public_ip6_server': 'https://app6.pritunl.com/ip',
        'notification_server': 'https://app.pritunl.com/notification',
        'update_check_rate': 3600,
        'session_limit': 16,
        'session_timeout': 43200,
        'peer_limit': 500,
        'peer_limit_timeout': 10,
        'log_limit': 10000,
        'log_entry_limit': 50,
        'log_db_delay': 1,
        'log_web_errors': False,
        'rate_limit_sleep': 0.5,
        'short_url_length': 8,
        'long_url_length': 16,
        'license': None,
        'license_plan': None,
        'http_request_timeout': 15,
        'request_queue_size': 10,
        'request_thread_count': 50,
        'request_max_thread_count': 250,
        'request_accepted_queue_size': 50,
        'static_cache_time': 43200,
        'auth_time_window': 86400,
        'auth_limiter_ttl': 60,
        'auth_limiter_count_max': 15,
        'org_pool_size': 1,
        'user_pool_size': 6,
        'server_pool_size': 4,
        'server_user_pool_size': 2,
        'dh_param_bits_pool': [1536],
        'cookie_secret': None,
        'cookie_secret2': None,
        'email_server': None,
        'email_username': None,
        'email_password': None,
        'email_from': None,
        'id': None,
        'sso': False,
        'sso_cache': True,
        'sso_cache_timeout': 28800,
        'sso_whitelist': [],
        'sso_client_cache': False,
        'sso_client_cache_timeout': 172800,
        'sso_client_cache_window': 21600,
        'sso_match': None,
        'sso_timeout': 60,
        'sso_org': None,
        'sso_google_mode': 'org',
        'sso_google_key': None,
        'sso_google_email': None,
        'sso_saml_url': None,
        'sso_saml_issuer_url': None,
        'sso_saml_cert': None,
        'sso_okta_token': None,
        'sso_okta_poll_rate': 0.25,
        'sso_okta_push': True,
        'sso_okta_skip_unavailable': True,
        'sso_onelogin_key': None,
        'sso_onelogin_id': None,
        'sso_onelogin_secret': None,
        'sso_onelogin_region': 'us',
        'sso_onelogin_push': False,
        'sso_radius_prefix': None,
        'sso_radius_host': None,
        'sso_radius_secret': None,
        'sso_duo_host': None,
        'sso_duo_token': None,
        'sso_duo_secret': None,
        'sso_duo_mode': 'push_phone',
        'sso_duo_passcode_length': 6,
        'sso_yubico_servers': [
            'https://api.yubico.com/wsapi/2.0/verify',
            'https://api2.yubico.com/wsapi/2.0/verify',
            'https://api3.yubico.com/wsapi/2.0/verify',
            'https://api4.yubico.com/wsapi/2.0/verify',
            'https://api5.yubico.com/wsapi/2.0/verify',
        ],
        'sso_yubico_client': None,
        'sso_yubico_secret': None,
        'queue_low_thread_limit': 4,
        'queue_med_thread_limit': 2,
        'queue_high_thread_limit': 1,
        'host_ping': 10,
        'host_ping_ttl': 30,
        'theme': 'dark',
        'org_page_count': 5,
        'server_page_count': 3,
        'link_page_count': 10,
        'host_page_count': 10,
        'acme_api_url': 'https://acme-v01.api.letsencrypt.org',
        'acme_agreement_url': 'https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf',
        'acme_timestamp': None,
        'acme_key': None,
        'acme_domain': None,
        'acme_renew': 7171200,
        'server_cert': None,
        'server_key': None,
        'cloud_provider': None,
        'dns_server_restart': 21600,
        'aws_timeout': 3,
        'route53_region': None,
        'route53_zone': None,
        'us_east_1_access_key': None,
        'us_east_1_secret_key': None,
        'us_east_2_access_key': None,
        'us_east_2_secret_key': None,
        'us_west_1_access_key': None,
        'us_west_1_secret_key': None,
        'us_west_2_access_key': None,
        'us_west_2_secret_key': None,
        'us_gov_west_1_access_key': None,
        'us_gov_west_1_secret_key': None,
        'eu_west_1_access_key': None,
        'eu_west_1_secret_key': None,
        'eu_west_2_access_key': None,
        'eu_west_2_secret_key': None,
        'eu_central_1_access_key': None,
        'eu_central_1_secret_key': None,
        'ca_central_1_access_key': None,
        'ca_central_1_secret_key': None,
        'ap_northeast_1_access_key': None,
        'ap_northeast_1_secret_key': None,
        'ap_northeast_2_access_key': None,
        'ap_northeast_2_secret_key': None,
        'ap_southeast_1_access_key': None,
        'ap_southeast_1_secret_key': None,
        'ap_southeast_2_access_key': None,
        'ap_southeast_2_secret_key': None,
        'ap_south_1_access_key': None,
        'ap_south_1_secret_key': None,
        'sa_east_1_access_key': None,
        'sa_east_1_secret_key': None,
    }
