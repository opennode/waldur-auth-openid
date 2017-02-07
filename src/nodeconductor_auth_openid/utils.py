import logging

logger = logging.getLogger(__name__)


def get_civil_number(openid_identity):
    """
    Extract civil number from openID identity.
    Return empty string if personal code is not defined.

    Expected openid.identity value: https://openid.ee/i/EE:<personal_code>
    Example: https://openid.ee/i/EE:37605030299
    Only the last part (<personal_code>) is stored as civil number.
    """
    personal_code = openid_identity.split('/')[-1].split(':')[-1]
    if personal_code.isdigit():
        return personal_code
    else:
        logger.warning(
            'Unable to parse openid.identity {}: personal code is not a numeric value'.format(openid_identity))
        return ''
