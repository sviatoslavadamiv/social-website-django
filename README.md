# Social Website – Django Project

This project is a functional social bookmarking platform built with Django 5. It allows users to register, create profiles, share and like images, follow other users, and view activity streams in real time.

## Key Features
- **User Authentication**
  - Signup, login, logout
  - Password reset and change
  - Google login (OAuth 2)
- **User Profiles**
  - Profile page with avatar and birthday date
- **Image Bookmarking**
  - Add and share images with titles and descriptions
  - Bookmarklet for saving external content
  - Thumbnail generation
- **Social Features**
  - Like/unlike images (AJAX)
  - Follow/unfollow users (AJAX)
  - Personalized activity stream
- **Performance Tools**
  - Redis-based image view counting and ranking
  - Infinite scrolling
  - AJAX-based interactions