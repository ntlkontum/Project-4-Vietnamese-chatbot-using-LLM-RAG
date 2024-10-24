css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

botHTCN_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://scontent.fdad3-1.fna.fbcdn.net/v/t39.30808-6/453165472_478002988310506_2660168032393089821_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=IXlDDjAqH58Q7kNvgH3BkyT&_nc_ht=scontent.fdad3-1.fna&_nc_gid=AxixB2RvfmwQgdKHq2hx7_B&oh=00_AYDWOx7aDH2lOj-8LZcJBAoqCYyfeym9snprBhSH0G6vlg&oe=6701598E" >
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://th.bing.com/th/id/OIP.xSDeAf_dCpSln8f60zHcYQHaHa?rs=1&pid=ImgDetMain">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''