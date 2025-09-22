def send_tweet_with_images(api, text, image_paths):
    """
    Send a tweet with multiple images.

    Parameters:
    api: The Twitter API object.
    text: The text content of the tweet.
    image_paths: A list of file paths to the images to be uploaded.

    Returns:
    The response from the Twitter API after posting the tweet.
    """
    media_ids = []
    
    for image_path in image_paths:
        res = api.media_upload(image_path)
        media_ids.append(res.media_id_string)
    
    return api.update_status(status=text, media_ids=media_ids)