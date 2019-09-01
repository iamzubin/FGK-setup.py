#!/bin/python3

class Main():

        def __init__(self):
                
                # import system stuff
                import os
                import sys
                import json
                import pprint
                from ast import literal_eval

                # UI libs
                from PySide2 import QtCore, QtGui, QtWidgets
                from PyQt5 import QtCore, QtGui, QtWidgets

                # import UI
                from fgk import Ui_MainWindow
                from fgk import Ui_Login


                from pathlib import Path
                self.location_data = str(Path.home()) + "/.fgk"
                self.location_assets = "/usr/share/fedora-gooey-karma/"
                
                #  import Fedora libs
                from bodhi.client.bindings import BodhiClient
                from fedora.client import FasProxyClient, openidbaseclient

                
                self.username = None
                self.password = None
                self.login = False
                
                # init application
                app = QtWidgets.QApplication(sys.argv)
                MainWindow = QtWidgets.QMainWindow()
                self.error = QtWidgets.QApplication([])
                self.ui = Ui_MainWindow()
                self.ui.setupUi(MainWindow)
                
                # login window
                self.Login = QtWidgets.QDialog()
                self.ui_login = Ui_Login()
                self.ui_login.setupUi(self.Login)


                # set assets
                self.bugfix = QtGui.QPixmap(self.location_assets +"bugfix.png")
                self.enhancement = QtGui.QPixmap(self.location_assets + "enhancement.png")
                self.newpackage = QtGui.QPixmap(self.location_assets+"new_package.png")
                self.security = QtGui.QPixmap(self.location_assets + "security.png")
                
                # set listeners
                self.ui.listWidget.itemSelectionChanged.connect(self.selected)
                self.ui.lineEdit.textEdited.connect(self.searching)
                self.ui.pushButton.clicked.connect(self.postKarma)
                self.ui.fetchUpdatesButton.clicked.connect(self.fetchList)
                self.ui.nextButton.clicked.connect(self.next_page)
                self.ui.previousButton.clicked.connect(self.previous_page)


                # listeners loginPopup
                self.ui_login.saveButton.clicked.connect(self.save)

                
                # Get Login and fedora version
                self.loginPopup()

                # Bodhi
                self.bc = BodhiClient()
                self.fas = FasProxyClient()

                self.query_args = {}
                self.query_args['rows_per_page'] = 30
                self.query_args['page'] = 1
                
                # fedora Release
                self.fedoraRelease = self.bc.get_releases()
                self.release = []
                for i in self.fedoraRelease['releases']:
                        self.release.append(i['name'])
                self.ui_login.fedoraReleases.addItems(self.release)

                # setting buttons
                self.ui.pushButton.setEnabled(0)
                self.ui.loginButton.clicked.connect(self.loginPopup)

                # Misc
                self.critpath = False


                MainWindow.show()
                sys.exit(app.exec_())
        


        def loginPopup(self):
                self.Login.show()
                return(0)
        

        def save(self):
                
                self.username = self.ui_login.Username.text()
                self.password = self.ui_login.Password.text()
                self.query_args['releases'] = self.ui_login.fedoraReleases.currentText()
                self.Login.close()
                self.verifyLogin()
        
        def verifyLogin(self):
                verification = self.fas.verify_password(self.username, self.password)
                if(verification):
                        self.ui.usernamLable.setText(self.username)
                        self.ui.loginButton.setText("logout")
                        self.ui.loginButton.clicked.connect(self.logout)
                        self.login = True
                        self.ui.pushButton.setEnabled(1)
                else:
                        error_dialog = QtWidgets.QErrorMessage()
                        error_dialog.showMessage("Wrong Username or Password \n close to continue without login")
                        error_dialog.exec_()
                        self.loginPopup()

        def logout(self):
                self.username = None
                self.password = None
                self.login = None
                self.ui.usernamLable.setText("Username")
                self.ui.loginButton.setText("login")
                self.ui.loginButton.clicked.connect(self.loginPopup)
                self.ui.pushButton.setEnabled(0)


        
        
        # fetch the list of updates
        def fetchList(self, cached_data):
                try: 
                        self.ui.listWidget.clear()
                        if(cached_data):
                                self.data = json.load(open(cached_data, "r"))
                        else:
                                self.data = self.bc.query(**self.query_args)
                        for p in self.data['updates']:
                                self.ui.listWidget.addItem(p['title'])
                        self.cache()
                except Exception as e:
                        print(e)
                        pass


        # page controllers 
        def next_page(self):
                try:
                        self.query_args["page"] = int(self.query_args["page"]) + 1
                        self.ui.PageNum.setText(str(self.query_args["page"]))
                        self.directory = self.location_data + "/" +self.query_args['releases'] + '/'+ str(self.query_args['page']) + ".json"
                        self.fetchList(self.directory)
                        
                except Exception as e:
                        print(e)

        def previous_page(self):
                try:
                                
                        if (int(self.query_args["page"]) > 1):
                                self.query_args["page"] = int(self.query_args["page"]) - 1
                        self.ui.PageNum.setText(str(self.query_args["page"]))
                        self.directory = self.location_data + "/" +self.query_args['releases'] + '/'+ str(self.query_args['page']) + ".json"
                        
                        self.fetchList(self.directory)

                except Exception as e:
                        print(e)

        # cache function
        def cache(self):
                try:
                        self.directory = self.location_data + "/" +self.query_args['releases'] + '/'+ str(self.query_args['page']) + ".json"
                        
                        # check dir
                        os.makedirs(os.path.dirname( self.directory ), exist_ok=True)
                        with open(self.directory, "w") as f:
                                f.write(json.dumps(self.data))
                except Exception as e:
                        print(e)

        # custom comment function for critpath
        def comment(self, update, comment, karma=0, critpath = None):
                try:
                        if (critpath == None):
                                x = self.bc1.send_request('comments/', verb='POST', auth=True, data={'update': update, 'text': comment, 'karma': karma, 'csrf_token': self.bc1.csrf()})
                        else:
                                x = self.bc1.send_request('comments/', verb='POST', auth=True, data={'update': update, 'text': comment, 'karma': karma, 'karma_critpath': critpath ,'csrf_token': self.bc1.csrf()})
                        return(x)
                except Exception as e:
                        print(e)

        def postKarma(self):
                t = self.ui.Package_breif.text()
                print(t)
                if (not self.login):
                                error_dialog = QtWidgets.QErrorMessage()
                                error_dialog.showMessage("login before posting karma")
                                error_dialog.exec_()
                else:
                        try:
                                if(self.critpath == True):
                                        self.bc1 = BodhiClient(base_url='https://bodhi.fedoraproject.org/', username=self.username, password=self.password)
                                        response = self.comment(t, self.ui.commentEdit.toPlainText(), self.ui.karmaBox.currentText(),self.ui.critpathBox.currentText())
                                elif(self.critpath == False):
                                        self.bc1 = BodhiClient(base_url='https://bodhi.fedoraproject.org/', username=self.username, password=self.password)
                                response = self.comment(t, self.ui.commentEdit.toPlainText(), self.ui.karmaBox.currentText())
                                error_dialog = QtWidgets.QErrorMessage()
                                error_dialog.showMessage("Karma Posted")
                                error_dialog.exec_()
                        
                        except Exception as e:
                                print(e)
                                error_dialog = QtWidgets.QErrorMessage()
                                error_dialog.showMessage(str(e))
                                error_dialog.exec_()



        # selecting the update

        # populates comments in the section
        def populateComments(self, t):
                try:
                        for comments in t['comments']:
                                comment = QtWidgets.QTreeWidgetItem()
                                comment.setText(0, str(comments['id']))
                                comment.setText(1, str(comments['karma']))
                                comment.setText(2, str(comments['karma_critpath']))
                                comment.setText(3, str(comments['user']['name']))
                                comment.setText(4, str(comments['text']))
                                self.ui.treeWidget_comment.insertTopLevelItem(0,comment)
                except:
                        pass
        



        # changes the display text on selection.
        def selected(self):
                try:
                        t = self.ui.listWidget.selectedItems()
                        for p in self.data['updates']:
                                if p['title']== t[0].text():
                                        self.ui.Package_name_main.setText(p['title'])
                                        self.ui.Package_breif.setText(p['alias'])
                                        self.ui.Status.setText(p['status'])
                                        self.ui.Date_submitted.setText(p["date_submitted"])
                                        self.ui.Submit_user.setText(p['user']['name'])
                                        self.ui.Request.setText(p['request'])
                                        self.ui.Karma.setText(str(p['karma']))
                                        self.ui.Release_notes.setText(p['notes'])
                                        self.ui.treeWidget_comment.clear()
                                        self.populateComments(p)
                                        if(p["type"] == "enhancement"):  
                                                self.ui.UpdateType.setPixmap(self.enhancement)
                                        elif(p["type"] == "bugfix"):
                                                self.ui.UpdateType.setPixmap(self.bugfix)                                                
                                        elif(p["type"] == "security"):
                                                self.ui.UpdateType.setPixmap(self.security)                                                
                                        elif(p["type"] == "newpackage"):
                                                self.ui.UpdateType.setPixmap(self.newpackage)
                                        
                                        if(p['critpath'] == True):
                                                self.ui.critpathBox.setVisible(1)
                                                self.ui.critpathText.setVisible(1)
                                                self.critpath = True
                                        if(p['critpath'] == False):
                                                self.ui.critpathBox.setVisible(0)
                                                self.ui.critpathText.setVisible(0)
                                                self.critpath = False


                except Exception as e:
                        print(e)
                        pass

        
        # using the search bar
        def searching(self):
                try:
                        self.ui.listWidget.clear()
                        for p in self.data['updates']:
                                if str(self.ui.lineEdit.text()) in p['title']:
                                        self.ui.listWidget.addItem(p['title'])
                        pass
                except Exception as e:
                        print(e)


def main():
        app = Main()
if __name__ == "__main__":
        main()