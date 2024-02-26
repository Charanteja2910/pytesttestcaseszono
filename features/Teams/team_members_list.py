from settings.api_requests import getApi
from settings.conftest import main_url
from user.test_login import main_workspace


def get_teams_list():
    url = f"{main_url}/teams/list/{main_workspace[0]["cwId"]}?includeCustomerGroups=true&workspaceId={main_workspace[0]["cwId"]}&includeInactive=true&includePendingInvites=true&includeTeamCustomersMapping=true"
    res = getApi(url)
    return res