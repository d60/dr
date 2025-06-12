from datetime import datetime

from config import config


def build_form_data(from_unix, to_unix, menu_id):
    return {
        'email': config['email'],
        'orgId': config['org_id'],
        'menuId': menu_id,
        'startAt': datetime.utcfromtimestamp(from_unix).isoformat(timespec='milliseconds') + 'Z',
        'endAt': datetime.utcfromtimestamp(to_unix).isoformat(timespec='milliseconds') + 'Z',
        'startAtUnixSecond': from_unix,
        'endAtUnixSecond': to_unix,
        'reservationName': config['name'],
        'reservationKanaName': '',
        'tel': config['tel'],
        'message': '',
        'customFormSchema': {
            'root': [
                {
                    'id': 'ip2z',
                    'title': '',
                    'children': [
                        {
                            'id': 'dv98',
                            'enum': [
                                {
                                    'text': '英語',
                                    'value': '英語'
                                },
                                {
                                    'text': 'スペイン語',
                                    'value': 'スペイン語'
                                },
                                {
                                    'text': 'ペルシャ語',
                                    'value': 'ペルシャ語'
                                },
                                {
                                    'text': '韓国語',
                                    'value': '韓国語'
                                },
                                {
                                    'text': '中国語',
                                    'value': '中国語'
                                },
                                {
                                    'text': 'ポルトガル語',
                                    'value': 'ポルトガル語'
                                },
                                {
                                    'text': 'ロシア語',
                                    'value': 'ロシア語'
                                },
                                {
                                    'text': 'タイ語',
                                    'value': 'タイ語'
                                },
                                {
                                    'text': 'タガログ語',
                                    'value': 'タガログ語'
                                },
                                {
                                    'text': 'ベトナム語',
                                    'value': 'ベトナム語'
                                },
                                {
                                    'text': 'インドネシア語',
                                    'value': 'インドネシア語'
                                },
                                {
                                    'text': 'クメール語',
                                    'value': 'クメール語'
                                },
                                {
                                    'text': 'ネパール語',
                                    'value': 'ネパール語'
                                },
                                {
                                    'text': 'ミャンマー語',
                                    'value': 'ミャンマー語'
                                },
                                {
                                    'text': 'モンゴル語',
                                    'value': 'モンゴル語'
                                },
                                {
                                    'text': 'ウクライナ語',
                                    'value': 'ウクライナ語'
                                },
                                {
                                    'text': 'シンハラ語',
                                    'value': 'シンハラ語'
                                },
                                {
                                    'text': 'ウルドゥー語',
                                    'value': 'ウルドゥー語'
                                },
                                {
                                    'text': 'アラビア語',
                                    'value': 'アラビア語'
                                },
                                {
                                    'text': 'ヒンディー語',
                                    'value': 'ヒンディー語'
                                }
                            ],
                            'label': {
                                'text': '外国語問題',
                                'shouldDisplay': True
                            },
                            'hidden': False,
                            'required': False,
                            'inputType': 'select',
                            'description': {
                                'text': '外国語で受験を希望する場合は選択してください。',
                                'shouldDisplay': True
                            },
                            'elementType': 'input',
                            'validations': []
                        },
                        {
                            'id': 'r7c0',
                            'enum': [
                                {
                                    'text': '受験案内票が必要なことを確認しました',
                                    'value': '受験案内票が必要なことを確認しました'
                                }
                            ],
                            'label': {
                                'text': '受験案内票の作成について',
                                'shouldDisplay': True
                            },
                            'hidden': False,
                            'required': True,
                            'inputType': 'radio_buttons',
                            'description': {
                                'text': '受験するためには受験案内票が必要です。\nお持ちでない方は予約完了メールに記載のＵＲＬから作成してください。',
                                'shouldDisplay': True
                            },
                            'elementType': 'input',
                            'validations': []
                        }
                    ],
                    'elementType': 'section'
                }
            ],
            'version': '1.0.0',
            'conditionalRuleSet': {
                'conditionalRules': []
            }
        },
        'customFormData': {
            'r7c0': '受験案内票が必要なことを確認しました'
        }
    }
