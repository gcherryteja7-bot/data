< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Student
Login
Portal < / title >
< style >
*{
    margin: 0;
padding: 0;
box - sizing: border - box;
font - family: 'Segoe UI', Tahoma, Geneva, Verdana, sans - serif;
}

body
{
    background: linear - gradient(135deg,  # 1a2980, #26d0ce);
min - height: 100
vh;
display: flex;
justify - content: center;
align - items: center;
padding: 20
px;
}

.container
{
    background - color: white;
width: 100 %;
max - width: 500
px;
border - radius: 15
px;
box - shadow: 0
15
px
30
px
rgba(0, 0, 0, 0.2);
overflow: hidden;
}

.header
{
    background - color:  # 2c3e50;
        color: white;
padding: 25
px;
text - align: center;
}

.header
h1
{
    font - size: 28px;
margin - bottom: 5
px;
}

.header
p
{
    opacity: 0.8;
}

.form - container
{
    padding: 30px;
}

.form - group
{
    margin - bottom: 20px;
}

label
{
    display: block;
margin - bottom: 8
px;
font - weight: 600;
color:  # 333;
}

input, select
{
    width: 100 %;
padding: 12
px
15
px;
border: 1
px
solid  # ddd;
border - radius: 8
px;
font - size: 16
px;
transition: border - color
0.3
s;
}

input: focus, select: focus
{
    border - color:  # 3498db;
        outline: none;
box - shadow: 0
0
0
2
px
rgba(52, 152, 219, 0.2);
}

.radio - group
{
    display: flex;
gap: 20
px;
margin - top: 5
px;
}

.radio - option
{
    display: flex;
align - items: center;
gap: 8
px;
}

.radio - option
input
{
    width: auto;
}

.submit - btn
{
    background - color:  # 3498db;
        color: white;
border: none;
padding: 15
px;
font - size: 18
px;
font - weight: 600;
border - radius: 8
px;
cursor: pointer;
width: 100 %;
margin - top: 10
px;
transition: background - color
0.3
s;
}

.submit - btn: hover
{
    background - color:  # 2980b9;
}

.blue - background
{
    background - color:  # 1a2980 !important;
        color: white !important;
}

.footer
{
    text - align: center;
padding: 20
px;
color:  # 666;
font - size: 14
px;
border - top: 1
px
solid  # eee;
}

.message
{
    padding: 15px;
border - radius: 8
px;
margin - bottom: 20
px;
text - align: center;
display: none;
}

.success - message
{
    background - color: rgba(46, 204, 113, 0.2);
color:  # 27ae60;
border: 1
px
solid  # 2ecc71;
}

@media(max - width

: 600
px) {
.container
{
    max - width: 100 %;
}

.form - container
{
    padding: 20px;
}

.radio - group
{
    flex - direction: column;
gap: 10
px;
}
}
< / style >
    < / head >
        < body >
        < div


class ="container" id="mainContainer" >

< div


class ="header" >

< h1 > Student
Login
Portal < / h1 >
< p > Enter
your
details
to
access
student
services < / p >
< / div >

< div


class ="form-container" >

< div
id = "successMessage"


class ="message success-message" >

< strong > Login
Successful! < / strong > Your
details
have
been
submitted.
< / div >

< form
id = "studentForm" >
< div


class ="form-group" >

< label
for ="name" > Full Name < / label >
< input
type = "text"
id = "name"
name = "name"
placeholder = "Enter your full name"
required >
< / div >

< div


class ="form-group" >

< label
for ="regNo" > Registration Number < / label >
< input
type = "text"
id = "regNo"
name = "regNo"
placeholder = "Enter your registration number"
required >
< / div >

< div


class ="form-group" >

< label > Hostel / Day
Scholar < / label >
< div


class ="radio-group" >

< div


class ="radio-option" >

< input
type = "radio"
id = "hostel"
name = "accommodation"
value = "hostel"
checked >
< label
for ="hostel" > Hostel < / label >
< / div >
< div


class ="radio-option" >

< input
type = "radio"
id = "dayScholar"
name = "accommodation"
value = "dayScholar" >
< label
for ="dayScholar" > Day Scholar < / label >
< / div >
< / div >
< / div >

< button
type = "submit"


class ="submit-btn" id="submitBtn" > Submit Login < / button >

< / form >
< / div >

< div


class ="footer" >

< p >© 2023
Student
Portal.All
rights
reserved. < / p >
< / div >
< / div >

< script >
document.getElementById('studentForm').addEventListener('submit', function(event)
{
    event.preventDefault();

// Get
form
values
const
name = document.getElementById('name').value;
const
regNo = document.getElementById('regNo').value;
const
accommodation = document.querySelector('input[name="accommodation"]:checked').value;

// Validate
form
if (name.trim() === '' | | regNo.trim() == = '') {
    alert('Please fill in all required fields');
return;
}

// Change
background
to
blue
document.body.classList.add('blue-background');

// Show
success
message
const
successMessage = document.getElementById('successMessage');
successMessage.style.display = 'block';

// Change
button
text and disable
it
const
submitBtn = document.getElementById('submitBtn');
submitBtn.textContent = 'Submitted Successfully!';
submitBtn.disabled = true;
submitBtn.style.backgroundColor = '#27ae60';

// Display
submitted
data in console
console.log('Student Login Details:');
console.log('Name:', name);
console.log('Registration Number:', regNo);
console.log('Accommodation:', accommodation == = 'hostel' ? 'Hostel': 'Day Scholar');

// Optional: Reset
form
after
3
seconds
setTimeout(() = > {
                  // Reset
form
document.getElementById('studentForm').reset();

// Re - enable
button and reset
text
submitBtn.textContent = 'Submit Login';
submitBtn.disabled = false;
submitBtn.style.backgroundColor = '';

// Hide
success
message
successMessage.style.display = 'none';

// Remove
blue
background
document.body.classList.remove('blue-background');
}, 5000);
});

// Form
field
validation
on
input
document.getElementById('name').addEventListener('input', function()
{
if (this.value.trim() !== '')
{
this.style.borderColor = '#2ecc71';
} else {
this.style.borderColor = '#ddd';
}
});

document.getElementById('regNo').addEventListener('input', function()
{
if (this.value.trim() !== '')
{
this.style.borderColor = '#2ecc71';
} else {
this.style.borderColor = '#ddd';
}
});
< / script >
    < / body >
        < / html >