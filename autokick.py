import weechat

weechat.register('autokick', 'xiong_chiamiov', '0.1', 'WTFPL', 'Autokick users if they try to get a botlist.', '', '')

def kick_on_botlist_request(data, signal, signal_data):
	info = weechat.info_get_hashtable('irc_parse_message', {'message': signal_data})
	
	nick = info['nick']
	server = signal.split(",")[0]
	channel = info['channel']
	buffer = weechat.info_get("irc_buffer", "%s,%s" % (server, channel))
	#weechat.prnt(buffer, 'info: %s' % info)
	message = info['arguments'].split(':', 1)[1].strip()

	if message.startswith(('list', 'find', 'blist'), 1) \
	or message.startswith('xdcc list'):
		weechat.command(buffer, '/kick %s No list/find/xdcc list!' % nick)

	return weechat.WEECHAT_RC_OK

weechat.hook_signal('*,irc_in2_privmsg', 'kick_on_botlist_request', '')

