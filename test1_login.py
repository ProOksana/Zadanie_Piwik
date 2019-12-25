import pytest
from fields import Fields
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    app.populating_fields(Fields(firstname="Oksana", lastname="Prokopek"))
    app.submit_data()


def test_empty_login(app):
    app.populating_fields(Fields(firstname="", lastname=""))
    app.submit_data()


def test_with_enter(app):
    app.populating_fields(Fields(firstname="   ", lastname="   "))
    app.submit_data()


def test_spec_char(app):
    app.populating_fields(Fields(firstname="d426373!@#$%^&*()_+}{:?><", lastname="d426373!@#$%^&*()_+}{:?><"))
    app.submit_data()


def test_max_length(app):
    app.populating_fields(Fields(firstname="Start khgkudhfuhgkdfhog sldnvgldjnrgjndjlfngbjdnlbjngfnkjngfbkjnkjg73ryehwifhrkghdf"
                                             "sfhvbksbfkuksvbnfkskbfndkndbknkdunfknkdbjfkdurotiguw48t938w4u98tugef948ug9e8r9hu8rth"
                                             "dufhbogudofbuijdotibjoeitjboinjtrnojhtboiejr8ot3 oiwrjgo3ij4oe59hjr0e59jh950hjr9t50h riej"
                                             "eirojgboeirjboijetoibjojgtrnoibjrgoijrjntoietoigjot83u4r5o38409 iwvngoierngoienrooijgierjg"
                                             "ijbgoiejtbiojrtiobjrjtonirjtnoijroijtnoirjtniojoryitnjoityjnoirjtnjrtptjprjthpbeojpteeEND",
                               lastname="Start sfnlbdnflbjidofijtb slkrjgbe djfnbldnlfkblkdgmnlbknijroiobdjgtijcvjbnkjdngkjbngfkbjn"
                                        "dfkbmlkngflbjkgfnnlkfgklmflkgmnlkfmgnmkllfkmgobn ksjdngvkjsnkdvbf fjnvglbdjfnbljnclgbkn"
                                        "djfnbjdngbljndlgknblkdnglkbmldkmnlkndflkbnlgjnlbngfbkdjgkbjkf dlkfbhjldjitglhdjgfblknldkg"
                                        "df;kmblkdgmblkmdglknmlfmdfhbndljtnguheotoy8e5roigj jrglidjflhigdlj ldjgldjigjpdifjgnl djvnfds"
                                        "lsnfvblksnlfsm fdsjbnlsijrojifwoeurjoqw83u4982398ru49i7ytei547yt985ue9y804e58tguoerghero"))
    app.submit_data()


def test_enter_link(app):
    app.populating_fields(Fields(firstname="http://www.montypython.com/", lastname="http://www.montypython.com/"))
    app.submit_data()
