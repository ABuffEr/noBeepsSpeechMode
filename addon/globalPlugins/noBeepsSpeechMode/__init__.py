# -*- coding: UTF-8 -*-
#Plugin to switch only between Talk or Off speech modes
#Author: Alberto Buffolino

import addonHandler
import globalPluginHandler
import speech
import msg
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_noBeepsSpeechMode(self, gesture):
		curMode=speech.speechMode
		if curMode==speech.speechMode_talk:
			# change order of two next lines of code to having no speech message about off
			# (direct off mode, with only Braille message, if active)
			# Translators: no translation required (see msg.py)
			msg.message("speech mode off")
			speech.speechMode=speech.speechMode_off
		elif curMode==speech.speechMode_off:
			speech.speechMode=speech.speechMode_talk
			# Translators: no translation required (see msg.py)
			msg.message("speech mode talk")

	# Translators: Message presented in input help mode,
	# this string is partially present in .po localization file of NVDA for the various languages.
	script_noBeepsSpeechMode.__doc__=_("Toggles between the speech modes of off and talk. When set to off NVDA will not speak anything. If talk then NVDA wil just speak normally.")

	__gestures = {
		"kb:NVDA+s": "noBeepsSpeechMode",
	}