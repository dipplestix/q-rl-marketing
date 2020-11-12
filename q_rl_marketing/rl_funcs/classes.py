class Person:
    def __init__(self, cid, status, name, title, company, email, phone, source, last_contact):
        self.cid = cid
        self.status = status
        self.name = name
        self.title = title
        self.company = company
        self.email = email
        self.phone = phone
        self.source = source
        self.last_contact = last_contact
        self.newsletters = 0
        self.webinars_invited = 0
        self.dai_invites = 0
        self.dai_user = 0
        self.nurture = 0
        self.reports = 0
        self.emails_sent = 0
        self.emails_opened = 0
        self.webinars_attended = 0
        self.state = self.get_state()
        self.actions = []
        self.results = []

    def action(self, action):
        if action == 'Send Newsletter':
            self.emails_sent += 1
            self.newsletters += 1
        if action == 'Add to email Nurture campaigns':
            self.nurture += 1
            self.emails_sent += 1
        if action == 'Send email invite to upcoming webinar':
            self.webinars_invited += 1
            self.emails_sent += 1
        if action == 'Invite to Driverless AI free trial':
            self.emails_sent += 1
            self.dai_invites += 1
        if action == 'Send email with Analyst Report':
            self.reports += 1
            self.emails_sent += 1
        if action == 'None':
            pass
        self.actions.append(action)

    def log(self, results):
        for result in results:
            if result == 'Started DAI trial':
                self.dai_user = 1
            if result == 'Attended Webinar':
                self.webinars_attended += 1
            if result == 'Opened e-mail':
                self.emails_opened += 1
        self.results.append(results)


    def get_state(self):
        return tuple([self.emails_sent, self.emails_opened, self.webinars_attended, self.dai_user])
