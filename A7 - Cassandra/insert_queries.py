columns={}
columns['tweets_by_tid']=('author', 'author_id', 'author_profile_image', 'author_screen_name', 'hashtags', 'keywords_processed_list', 'lang', 'like_count', 'location', 'media_list', 'mentions', 'quote_count', 'quoted_source_id', 'reply_count', 'replyto_source_id', 'retweet_count', 'retweet_source_id', 'sentiment', 'tid', 'tweet_text', 'tweet_date', 'tweet_datetime', 'type', 'url_list', 'verified' )
# columns['tweets_by_author']=('author', 'author_id', 'author_screen_name', 'lang', 'location', 'tid', 'tweet_text', 'tweet_date', 'tweet_datetime', 'like_count', 'author_profile_image', 'hashtags', 'keywords_processed_list', 'media_list', 'mentions', 'quote_count', 'quoted_source_id', 'reply_count', 'replyto_source_id', 'retweet_count', 'retweet_source_id', 'sentiment', 'type', 'url_list', 'verified' )
# columns['tids_by_author']=('author', 'author_id', 'author_screen_name', 'tid', 'tweet_date', 'tweet_datetime' )
# columns['tids_by_date']=('tweet_date', 'tweet_datetime', 'tid' )
# columns['tids_by_location']=('location', 'tid', 'tweet_date', 'tweet_datetime' ) 
# # Contains some custom columns-
# columns['tids_by_hashtag']=('hashtag', 'tid', 'tweet_date', 'tweet_datetime' ) 
# columns['tids_by_mention']=('m_author', 'tid', 'tweet_date', 'tweet_datetime' ) 
# columns['hashtag_counter']=('hash_week', 'hash_date', 'hashtag', 'hashtag_count' ) 
statements={}
for table in columns.keys():
	cols=columns[table]
	statements[table]="insert into twitterdb."+table+" ("+",".join(cols)+") values (" + "?,"*(len(cols)-1)+"?" + ") if not exists";