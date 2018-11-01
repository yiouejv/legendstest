var num = 5;
		function redirect() {
			num--;
			document.getElementById("num").innerHTML = num;
			if(num < 0) {
				document.getElementById("num").innerHTML = 0;
				location.href = "/";
			}
		}
		setInterval("redirect()", 1000);